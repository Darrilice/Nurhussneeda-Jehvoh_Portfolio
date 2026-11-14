# Thai royal duties word clouds

**Year 2 · Getting and Cleaning Data · Thai text processing, PyThaiNLP, visualisation**

## Primary evidence and code status

The ten original word-cloud PNGs in [`result/`](result/) are the project outcome. No report was recovered. `script/R1.ipynb` shows the method for Rama I; code for all ten final images was not recovered.

## Dataset and workflow

`dataset/` contains ten Thai text files about royal duties for Rama I–X. The surviving notebook uses PyThaiNLP tokenisation and stop-word filtering before making a word cloud.

## End-to-end workflow

Collect text by reign → split Thai words → remove stop words → generate one word cloud per reign. The notebook uses older filenames and a local font path, so it does not reproduce all ten images as-is.

## Results and outcome

**Ten word clouds** show frequent terms in the collected text. Word size reflects filtered word frequency; no quantitative model evaluation was recorded.

## Saved historical results

[`Rama1.png` through `Rama10.png`](result/) are the saved final outputs.

## Files

[`dataset/`](dataset/) · [`script/R1.ipynb`](script/R1.ipynb) · [`result/`](result/). No report is available.
