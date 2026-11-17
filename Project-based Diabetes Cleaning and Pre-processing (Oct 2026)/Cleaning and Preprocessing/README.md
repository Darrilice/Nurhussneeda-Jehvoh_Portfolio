# Cleaning and Preprocessing

## Purpose

I prepared a consistent set of outpatient diabetes tables that analysts could join, validate and reuse. The work also produced an HbA1c cohort for longitudinal analysis and derived BMI and estimated average glucose (eAG) from source measurements.

## Inputs

| Source | Contents and role |
| --- | --- |
| Height and weight | Body measurements used to derive BMI and patient-level measurement summaries. |
| Outpatient visits (OPD) | Visit dates, demographic context, clinic fields and diagnosis codes. Distinct visit dates were used for cohort selection. |
| Outpatient medication | Prescription dates and medication items used in downstream longitudinal analysis. |
| Laboratory results (LAB) | Test names, dates and results. Numeric HbA1c results were used to derive eAG. |
| DTX | Glucose readings recorded with clinic and visit dates. |

## Processing steps

1. **Profile the raw extracts.** Read the five CSVs as text to preserve codes and missing markers. Inspect schema, value counts, missingness, exact duplicates, date coverage, numeric ranges and code-to-label consistency.
2. **Standardize fields.** Normalize dates and numeric representations using configurable rules. Apply label mappings where available, remove exact duplicate rows, add row identifiers for traceability and use patient-level height and weight summaries where specified. Keep missing and invalid measurements identifiable for later validation.
3. **Join LAB and DTX.** Use a full outer join on the patient key and keep both source dates. A patient with multiple results in both tables can contribute multiple joined combinations. The joined table records LAB-only, DTX-only and matched rows, and retains each source date for interpretation.
4. **Derive analysis fields.** Calculate BMI from height and weight and a separate BMI from patient-level mean measurements. For qualifying HbA1c results, calculate eAG in mg/dL as `28.7 × HbA1c − 46.7`, then convert to mmol/L using the project conversion factor.
5. **Select the HbA1c cohort.** Require at least two distinct outpatient visit dates and at least one numeric result for a test named HbA1c. The cohort LAB and joined exports keep qualifying HbA1c rows. The other cohort tables retain relevant records for qualifying patients.
6. **Validate and export.** Check schema, identifiers, dates, numeric types and ranges, derived formulas, join states and cohort membership. Export validated tables with metadata and record validation results and stage counts in the run summary.

## Results and handover

The pipeline produced **three versions of the six-table output**: cleaned, preprocessed and HbA1c cohort. Each version contains the five source-derived tables plus the LAB–DTX join. Metadata describes row counts, field types and missingness, and a cohort summary supports before-and-after profiling. The HbA1c cohort became the input for the [Medical Response Dataset](../Medical%20Response%20Dataset/README.md).

### **-- Skills and tools --**
#### Python, pandas, exploratory data analysis, schema standardization, CSV processing, joins, cohort design, data validation and metadata generation.
