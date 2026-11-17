# Medical Response Dataset

## Purpose

I built a longitudinal dataset so analysts could explore how estimated average glucose (eAG) changed over time for each patient and medication pair. The dataset provides two comparison points for the same series: the preceding eligible result and the first eligible result on or after the first recorded prescription date.

## Inputs and unit of analysis

The notebook uses the validated [HbA1c cohort](../Cleaning%20and%20Preprocessing/README.md). Outpatient prescriptions provide medication items and recorded prescription dates, laboratory records provide dated HbA1c-derived eAG in mmol/L, and outpatient and measurement tables provide demographic and body-measurement context. The analysis unit is one eligible laboratory event for one patient–medication pair. A patient with multiple medication items can contribute separate timelines, and the same LAB event can appear in more than one timeline.

## Workflow

1. **Identify each pair.** Parse dates and drop prescription rows without a usable date or medication item. Group by patient and medication item, and use the earliest recorded prescription date for the pair.
2. **Prepare laboratory events.** Keep records with a usable LAB date and numeric eAG, and deduplicate repeated entries using patient, LAB date and eAG. Attach the latest usable outpatient context, with measurement-table fallback where applicable.
3. **Build the timeline.** Join by patient, keep LAB events on or after the first recorded prescription date and sort the events chronologically within each pair.
4. **Calculate eAG change.** Subtract either the previous eligible result or the first eligible result for that pair from the current eAG. Record whether eAG decreased, increased or stayed unchanged, and flag events without an available previous comparison.
5. **Export and summarize.** Produce event-level details, a pair-based summary output, visualization counts and plots of cohort characteristics, response direction and selected eAG trajectories.

| Comparison | Reference point | Question answered |
| --- | --- | --- |
| Current versus previous | Immediately preceding eligible LAB event in the same pair | How did eAG change since the previous eligible result? |
| Current versus first | First eligible LAB event on or after the recorded prescription date | How far has eAG moved from the first eligible result in the timeline? |

## Results and interpretation

The handover documented **five CSV outputs and 16 plots**. The two main comparisons each contained **627,718 patient–medication–LAB event rows**. These are repeated event rows across timelines. The resulting tables support descriptive analysis of eAG changes. Prescription records establish when an item was first recorded, and the comparison data describe observed trajectories. Estimating medication effects would require additional evidence about exposure, co-prescriptions and other factors that influence eAG.

### **-- Skills and tools --**
#### Python, Jupyter, longitudinal data preparation, date-based joins, deduplication, within-group comparisons, descriptive analysis and visualization.
