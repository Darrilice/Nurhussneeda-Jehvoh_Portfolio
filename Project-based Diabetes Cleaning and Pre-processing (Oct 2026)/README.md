# Diabetes Data Profiling, Cleaning and Preprocessing (October 2026) - Project-based work

## Purpose

The Rajavithi diabetes project needed consistent outpatient, medication and laboratory data for downstream analysis. I built a Python workflow that profiled the source extracts, standardized fields, prepared an HbA1c cohort and documented the quality of the exported datasets. I also built an exception report for numeric result fields and a longitudinal dataset for exploring estimated average glucose (eAG) after a recorded prescription.

## Data and scope

The source inventory included seven extracts. The main pipeline used five covering height and weight, outpatient visits, outpatient prescriptions, laboratory results and DTX glucose readings. Inpatient visits and inpatient medication were also present in the inventory. The five working extracts contained approximately **1.36 million source rows**. This is a count of records across files, including repeat visits and test results.

## Workflow and deliverables

| Workstream | What I built | Output |
| --- | --- | --- |
| [Cleaning and Preprocessing](Cleaning%20and%20Preprocessing/README.md) | Profiled and standardized five inputs, joined LAB and DTX, derived BMI and eAG and applied the HbA1c cohort rules. | Cleaned, preprocessed and HbA1c cohort exports, each with six tables and metadata. |
| [Unhandled Values](Unhandled%20Values/README.md) | Audited the raw LAB and DTX result fields for nonblank values the numeric parser could not interpret. | A detailed exception CSV and a grouped frequency summary covering 14 distinct LAB values. |
| [Medical Response Dataset](Medical%20Response%20Dataset/README.md) | Built timelines by patient and medication and compared eAG with the preceding result and with the first eligible result after the first recorded prescription. | Five CSV outputs and 16 plots in the project handover. |

The exception audit reads the raw result fields alongside the main pipeline. The medical response work uses the validated HbA1c cohort exported by that pipeline. The case studies describe the workflow and documented aggregate outputs. Patient-level data and source notebooks are held with the project.

## Project materials

- [Workflow diagram](Work_Flow.png)
- [Project presentation](report/presentation.pptx)
