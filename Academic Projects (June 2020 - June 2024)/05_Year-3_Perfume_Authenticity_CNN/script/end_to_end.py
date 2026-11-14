"""Run the perfume image-classification workflow for one or all brands.

The original project collected and labelled photographs of genuine and
counterfeit bottles. Those collected images are already in dataset/. This
script starts by auditing and loading those files. It does not take new photos.

Run from anywhere with:
    python script/end_to_end.py --brand all --epochs 30

Use --inventory-only to inspect the collected data without training a model.
New training results are written to result/reproduced/ and do not overwrite
the historical notebook outputs.
"""

import argparse
import csv
import json
from pathlib import Path


BRANDS = ("Dior", "Jomalone", "Versace")
SPLITS = ("train", "val", "test")
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 16
SEED = 42


def audit_images(dataset_root, brands):
    """Get the existing data and verify its split and real/fake labels."""
    rows = []
    for brand in brands:
        for split in SPLITS:
            split_dir = dataset_root / brand / split
            if not split_dir.is_dir():
                raise FileNotFoundError(f"Missing image split: {split_dir}")
            class_dirs = sorted(path for path in split_dir.iterdir() if path.is_dir())
            labels = {path.name.lower() for path in class_dirs}
            if labels != {"fake", "real"}:
                raise ValueError(f"Expected Fake and Real labels in {split_dir}, found {sorted(labels)}")
            for class_dir in class_dirs:
                images = sorted(path for path in class_dir.iterdir()
                                if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS)
                if not images:
                    raise ValueError(f"No images found in {class_dir}")
                rows.append({"brand": brand, "split": split,
                             "label": class_dir.name.lower(), "images": len(images)})
    return rows


def load_datasets(brand_dir):
    """Preprocess images as 224 x 224 RGB batches with binary labels."""
    import tensorflow as tf

    datasets = {}
    class_order = None
    for split in SPLITS:
        dataset = tf.keras.utils.image_dataset_from_directory(
            brand_dir / split,
            image_size=IMAGE_SIZE,
            batch_size=BATCH_SIZE,
            label_mode="binary",
            color_mode="rgb",
            shuffle=(split == "train"),
            seed=SEED if split == "train" else None,
        )
        normalized_names = tuple(name.lower() for name in dataset.class_names)
        if class_order is None:
            class_order = normalized_names
        if normalized_names != class_order or class_order != ("fake", "real"):
            raise ValueError(f"Inconsistent class order in {brand_dir / split}: {dataset.class_names}")
        datasets[split] = dataset.prefetch(tf.data.AUTOTUNE)
    return datasets


def build_cnn():
    """Augment training images, rescale pixels, and define a binary CNN."""
    import tensorflow as tf

    augmentation = tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal"),
        tf.keras.layers.RandomRotation(0.05),
        tf.keras.layers.RandomZoom(0.10),
        tf.keras.layers.RandomTranslation(0.10, 0.10),
    ], name="training_augmentation")

    model = tf.keras.Sequential([
        tf.keras.Input(shape=(*IMAGE_SIZE, 3)),
        augmentation,
        tf.keras.layers.Rescaling(1.0 / 255),
        tf.keras.layers.Conv2D(32, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(128, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dropout(0.30),
        tf.keras.layers.Dense(1, activation="sigmoid"),
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy",
                  metrics=["accuracy"])
    return model


def train_and_evaluate(brand, dataset_root, output_root, epochs):
    """Train, evaluate held-out images, and write the resulting outputs."""
    import numpy as np
    import tensorflow as tf
    from sklearn.metrics import classification_report, confusion_matrix

    tf.keras.utils.set_random_seed(SEED)
    data = load_datasets(dataset_root / brand)
    model = build_cnn()
    history = model.fit(
        data["train"],
        validation_data=data["val"],
        epochs=epochs,
        callbacks=[tf.keras.callbacks.EarlyStopping(
            monitor="val_loss", patience=5, restore_best_weights=True
        )],
        verbose=2,
    )

    # Random augmentation layers are inactive during evaluation and prediction.
    test_loss, test_accuracy = model.evaluate(data["test"], verbose=0)
    probabilities = model.predict(data["test"], verbose=0).ravel()
    actual = np.concatenate([labels.numpy().ravel() for _, labels in data["test"]]).astype(int)
    predicted = (probabilities >= 0.5).astype(int)
    matrix = confusion_matrix(actual, predicted, labels=[0, 1])
    report = classification_report(actual, predicted, labels=[0, 1],
                                   target_names=["fake", "real"], zero_division=0)

    output_dir = output_root / brand
    output_dir.mkdir(parents=True, exist_ok=True)
    metrics = {
        "brand": brand,
        "test_images": len(actual),
        "test_loss": float(test_loss),
        "test_accuracy": float(test_accuracy),
        "epochs_completed": len(history.history["loss"]),
        "class_order": ["fake", "real"],
        "seed": SEED,
    }
    (output_dir / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    (output_dir / "classification_report.txt").write_text(report, encoding="utf-8")
    with (output_dir / "confusion_matrix.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["actual\\predicted", "fake", "real"])
        writer.writerow(["fake", *matrix[0]])
        writer.writerow(["real", *matrix[1]])
    with (output_dir / "training_history.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        names = list(history.history)
        writer.writerow(["epoch", *names])
        for index in range(metrics["epochs_completed"]):
            writer.writerow([index + 1, *(history.history[name][index] for name in names)])
    print(f"{brand}: test accuracy {test_accuracy:.2%} on {len(actual)} images")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--brand", choices=(*BRANDS, "all"), default="all")
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--inventory-only", action="store_true")
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    if args.epochs < 1:
        parser.error("--epochs must be at least 1")

    brands = BRANDS if args.brand == "all" else (args.brand,)
    dataset_root = args.project_root / "dataset"
    output_root = args.output_dir or args.project_root / "result" / "reproduced"
    rows = audit_images(dataset_root, brands)
    for row in rows:
        print(f"{row['brand']:8} {row['split']:5} {row['label']:4} {row['images']:3} images")
    if args.inventory_only:
        return

    for brand in brands:
        train_and_evaluate(brand, dataset_root, output_root, args.epochs)


if __name__ == "__main__":
    main()
