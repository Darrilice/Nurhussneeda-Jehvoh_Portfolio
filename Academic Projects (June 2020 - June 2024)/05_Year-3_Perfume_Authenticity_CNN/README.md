# Perfume authenticity classification with CNN

**Year 3 · Image classification · Python, TensorFlow/Keras, OpenCV, image augmentation**

## Primary evidence and code status

The three original notebooks, their saved outputs and the original PDFs document the historical runs. [`script/end_to_end.py`](script/end_to_end.py) is a later reproducible workflow that reads the current folder paths; its results must be kept separate from the original notebook scores.

## Dataset and workflow

Manually collected real and fake photographs are split by brand and `train/`, `val/`, `test/` under `dataset/`. Dior has **316/89/47**, Versace **352/44/44**, and Jo Malone **280/80/40** train/validation/test images. Dior's training `real` folder uses lowercase; the newer script handles case differences.
#### Dataset Path (Have to extract files) : https://github.com/Darrilice/Nurhussneeda-Jehvoh_Portfolio/releases/tag/dataset-Perfume_Authenticity_CNN-v.1.0

## End-to-end workflow

Audit the collected images → load RGB images at **224 × 224** → augment training images → train a binary CNN with validation-based early stopping → evaluate untouched test images with accuracy, confusion matrix and classification report → save outputs under `result/reproduced/`.

From the project folder, run `python script/end_to_end.py --inventory-only` to audit data or `python script/end_to_end.py --brand all --epochs 30` to train. Image collection itself was manual, with no acquisition script.

## Results and outcome

The saved post-augmentation test accuracies are **Dior 46.81%**, **Versace 79.55%** and **Jo Malone 82.50%**. Dior performed poorly in the saved run. The Jo Malone notebook augments its test generator, so that historical score may vary if rerun.

## Saved historical results

| Brand | Test accuracy after augmentation | Test images |
|---|---:|---:|
| Dior | 46.81% | 47 |
| Versace | 79.55% | 44 |
| Jo Malone | 82.50% | 40 |

These values are saved notebook `Test Accuracy` outputs, transcribed in [`result/test-accuracy-after-augmentation.csv`](result/test-accuracy-after-augmentation.csv). No new training score is claimed here.

## Files

[`dataset/`](dataset/) · [`script/`](script/) · [`result/`](result/) · [`report/`](report/)
