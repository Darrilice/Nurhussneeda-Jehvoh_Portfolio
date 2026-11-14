# Normal and abnormal respiratory sounds

**Year 3 · Audio classification · Python, intended CNN workflow**

## Primary evidence and code status

The labelled WAV folders are the recoverable dataset. `script/breath 1.ipynb` stops during path setup; it contains no completed CNN training or evaluation. The original training run and its exact input paths cannot be verified.

## Dataset and workflow

Use the four class folders inside both splits: `train/Disease/` **184**, `train/Normal/` **84**, `test/Disease/` **47**, and `test/Normal/` **21** WAV files. These are **336 distinct examples**. Duplicate WAVs previously placed directly under `train/` and `test/` were removed; [`dataset/README.md`](dataset/README.md) explains the layout.

## End-to-end workflow

The intended task is binary classification of respiratory sounds as Disease or Normal. The recovered notebook imports audio and modelling libraries and begins data-path setup; preprocessing, CNN training and test evaluation are not present.

## Results and outcome

The class-labelled train/test dataset is available, but **no verified CNN accuracy** or saved model was recovered.

## Saved historical results

No training or evaluation output was found. [`result/README.md`](result/README.md) records that limitation.

## Files

[`dataset/`](dataset/) · [`script/breath 1.ipynb`](script/breath%201.ipynb) · [`result/README.md`](result/README.md). No report is available.
