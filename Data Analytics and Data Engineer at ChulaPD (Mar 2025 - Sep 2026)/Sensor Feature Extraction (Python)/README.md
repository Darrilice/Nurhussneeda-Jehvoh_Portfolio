# CheckPD Sensor Feature Extraction and Validation

## Purpose and my contribution

I built a Python workflow to convert smartphone motion recordings into numeric features for downstream research and model development. The project also tested which features could be computed reliably, how well they described variation within a CheckPD reference cohort and how recording duration affected stability.

## Input data and cohort

The source was CheckPD motion-test JSON. Each recording contained timestamps, three accelerometer axes and three gyroscope axes. The app had nine screening components. This analysis used the four motion recordings from a single session per participant. When multiple complete sessions were available, the workflow selected the latest eligible one.

The project sampled **1,000 participants** and retained **952 participant records** after file checks. The reference cohort consisted of participants the app classified as normal and for whom the study data recorded no physician diagnosis of Parkinson's disease or another movement disorder. Typical recordings lasted about **20 seconds** and had a sampling rate of about **40 Hz**, estimated from the timestamps in each recording.

## Processing workflow

1. **Select and validate each session.** Check file availability, timestamps, six-axis coverage and the minimum of 50 usable samples. Record why unusable files were skipped. Missing gyroscope channels were the main cause of skipped recordings.
2. **Prepare the signals.** Interpolate onto a regular time grid, use a zero-phase Butterworth high-pass filter to reduce gravity in accelerometer channels, and apply task-specific frequency filters. Compute Welch power spectral density for spectral features. Some variability measures use four-second windows with 50% overlap.
3. **Extract and document features.** Use shared Python signal-processing routines and task-specific extractors, with feature names and definitions tracked in four dictionaries. Run extraction in parallel and join results by participant. The dictionaries defined **715 candidate features** before filtering.
4. **Audit feature quality.** Check missing and non-finite values, expected bounds and implausible values such as negative energy. Use percentile-based flags for skewed feature distributions. Export feature tables, coverage summaries, skipped-file reports and outlier reports. The internal export used `999` as a missing-value marker, which was excluded from the modeling inputs.
5. **Compare feature sets and test reliability.** Compare a full candidate set and a curated set per task. Remove heavily missing and constant columns, filter incomplete and flagged rows, transform skewed features and use robust scaling. Compare K-means, Gaussian mixtures and Ward clustering across two to six clusters in the scaled and PCA-reduced spaces. Evaluate separation and cluster-size balance. Use split-half reliability to check the stability of features at the observed recording duration.

| Task | Candidate features | What they describe |
| --- | ---: | --- |
| Resting tremor | 327 | Motion amplitude, dominant frequency, band power and rhythmicity while the hand is at rest. |
| Postural tremor | 119 | Tremor amplitude, spectral peaks and variability while holding a position. |
| Standing balance | 140 | Sway amplitude, directional motion and variability during standing. |
| Walking | 129 | Cadence, step regularity and movement patterns, including arm swing and turning candidates. Turning features depended on whether the recording captured a usable turn. |

## Results

The eight clustering runs showed weak to moderate separation within the reference cohort. Balance gave the clearest separation and was the only task where the curated set improved silhouette. The curated sets used 13 to 18 features and made the trade-off between feature count and separation visible.

| Task | Full set: records / features / silhouette | Curated set: records / features / silhouette | Estimated reliability at about 20 seconds |
| --- | --- | --- | ---: |
| Resting tremor | 780 / 302 / 0.329 | 837 / 14 / 0.236 | 0.625 |
| Postural tremor | 813 / 119 / 0.255 | 883 / 15 / 0.222 | 0.499 |
| Standing balance | 911 / 140 / 0.427 | 909 / 13 / 0.475 | 0.334 |
| Walking | 839 / 125 / 0.303 | 855 / 18 / 0.219 | 0.683 |

The reliability estimates fell below the report's 0.70 reference threshold for each task. Standing balance had the lowest estimate. Short recordings limited the number of usable windows and gait cycles. Directional balance and gait features also depend on the assumed phone orientation.

I delivered participant-level feature tables, task-specific feature dictionaries and quality reports for researchers and data scientists to use in later work. Feature-importance and ROC analyses used the cluster assignments generated within this cohort as labels. Evaluating Parkinson's screening performance would require clinically labeled comparison cohorts processed through the same workflow.

*Source for aggregate results: the internal CheckPD Normal–Normal feature extraction report, sections 2, 5 and 7–12, and the associated clustering comparison summary.*
