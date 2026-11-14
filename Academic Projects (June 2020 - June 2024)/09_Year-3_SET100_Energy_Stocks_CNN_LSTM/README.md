# One-month SET100 energy stock forecasting

**Year 3 · Research Methods · CNN, LSTM, time-series modelling**

## Primary evidence and code status

The original report and three Colab notebooks document the historical CNN/LSTM comparison. The notebooks were recovered as extensionless JSON and saved with `.ipynb` names. Results quoted here come from the report, not a new training run.

## Dataset and workflow

`dataset/` has historical stock CSVs for **PTT, PTTEP and BCP**. The report describes an **80/20 train/test split** and a one-month adjusted-close forecasting horizon.

## End-to-end workflow

Prepare each stock series → make the reported train/test split → train CNN and LSTM models → forecast adjusted close → compare RMSE. The three original notebooks contain the modelling code; their old Colab paths may need updating to rerun locally.

## Results and outcome

The report's RMSE favoured **CNN for all three stocks**. Lower RMSE means lower reported prediction error for this comparison; the figures were not independently reproduced.

## Saved historical results

| Stock | LSTM RMSE | CNN RMSE |
|---|---:|---:|
| PTT | 1.6940 | 0.7330 |
| PTTEP | 11.3197 | 3.4429 |
| BCP | 4.6215 | 0.0192 |

The values are transcribed in [`result/rmse-from-report.csv`](result/rmse-from-report.csv); six original loss plots are in `result/loss/`.

## Files

[`dataset/`](dataset/) · [`script/`](script/) · [`result/`](result/) · [`report/`](report/)
