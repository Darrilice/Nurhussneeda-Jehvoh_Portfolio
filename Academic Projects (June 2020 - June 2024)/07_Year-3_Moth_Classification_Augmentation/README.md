# Moth classification and image augmentation

**Year 3 · Data Processing · TensorFlow/Keras, CNN, image augmentation**

## Primary evidence and code status

`script/10class_classification.ipynb` and `script/10class_augmentation.ipynb` are the original notebooks and contain the saved evaluation outputs. The filename `10class` is historical; the loaded data contain **50 species**.

## Dataset and workflow

The image folders contain 50 classes. Saved notebook output reports **7,183 training**, **250 validation** and **250 test** images. The baseline notebook loads 224 × 224 images, rescales them, trains a multiclass CNN and evaluates the test split; the second notebook adds image augmentation.

Dataset Path (Have to extract files) : https://github.com/Darrilice/Nurhussneeda-Jehvoh_Portfolio/releases/tag/dataset-Moth_Classification_Augmentation_v.1.0
## End-to-end workflow

Load labelled moth images → split train/validation/test → preprocess and train a baseline CNN → add augmentation in a comparison run → evaluate saved test outputs. Original E: drive paths require updating before a rerun.

## Results and outcome

The baseline reports **74% test accuracy**. The augmentation notebook prints **98%**, but it uses one sigmoid output and binary cross-entropy with 50-class categorical labels. That mismatch makes the 98% figure unreliable as 50-species accuracy.

## Saved historical results

Both scores are saved inside the notebooks; there is **no separate `result/` folder**. The course presentation is in `report/`.

## Files

[`dataset/`](dataset/) · [`script/`](script/) · [`report/presentation.pdf`](report/presentation.pdf)
