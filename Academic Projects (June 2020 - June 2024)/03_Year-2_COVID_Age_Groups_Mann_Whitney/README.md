# COVID-19 cases across two age groups

**Year 2 · Getting and Cleaning Data · Python, R, systematic sampling, Mann–Whitney test**

## Primary evidence and code status

Use [`report/Covid-19.pdf`](report/Covid-19.pdf) as the primary record. Only part of the preparation notebook survives; the original R sampling and Mann–Whitney scripts and complete result files were not recovered.

## Dataset and workflow

The report describes infected people aged **12–20** and **61–80**. `dataset/` contains the surviving case and age-group CSVs. `script/getting_data.ipynb` shows age filtering but references an absent input filename.

## End-to-end workflow

The report's sequence is: clean case records → filter the two age groups → take a **5,000-person systematic sample** → run a Mann–Whitney test at **0.05** significance. The full sequence cannot be rerun from the recovered code.

## Results and outcome

A reliable test statistic or p-value was not recovered, so the significance conclusion remains unverified. The data include infected people only and do not estimate general-population infection risk.

## Saved historical results

The report contains the original presentation of results; [`result/README.md`](result/README.md) records the missing test output.

## Files

[`dataset/`](dataset/) · [`script/getting_data.ipynb`](script/getting_data.ipynb) · [`report/Covid-19.pdf`](report/Covid-19.pdf) · [`result/`](result/)
