# Data Quality Improvement Project

## Objective

The project standardized self-entered demographic values for downstream analytics. I reviewed representative input patterns, developed field-specific Python transformations, and evaluated standardized formats and unresolved cases. The cloud workflow used S3 for storage and PySpark on Amazon EMR for distributed processing and validation.

## Workflow

1. Profile data for distinct formats, blanks, malformed values and recurring variants.
2. Define a standard output and develop transformations with regular expressions, dictionaries and field-specific validation.
3. Test the Python functions on example records and inspect the output status.
4. Run the distributed workflow on the configured cloud input and compare before-and-after counts and distributions.

The internship report covers 14 attributes. In addition to the seven fields below, it discusses email, phone number, language, ID card, passport number, address and name.

## Included notebooks

| Field | Method | Standardization improvement | What changed |
| --- | --- | --- | --- |
| [Gender](script/notebook_python/gender/gender.ipynb) | Normalize Thai and English labels into the supported gender categories. | ~+100 pp (0.023% to 100%) | 9 to 3 formats. Variants were consolidated into male, female and unknown. |
| [Marital Status](script/notebook_python/marital_status/marital_status.ipynb) | Map known Thai and English marital-status variants. | 0 pp (100% to 100%) | 5 to 4 formats. Married, widowed and single were retained, and unresolved variants were grouped as unknown. |
| [Education](script/notebook_python/education/education.ipynb) | Map recognized education abbreviations and labels by level. | 0% reported (no known values) | 1 to 1 format. The evaluated data remained unknown because no education values were supplied. |
| [Occupation](script/notebook_python/occupation/occupation.ipynb) | Standardize role and employment descriptions using text rules and mappings. | +96 pp (4% to 100%) | 19 to 18 formats. Role and employment variants were mapped to standard categories, with unknown retained. |
| [Nationality](script/notebook_python/nationality/nationality.ipynb) | Normalize country codes and compare unmatched names with dictionary entries. | +100 pp (0% to 100%) | 2 to 2 formats. The output categories were Thai and unknown. |
| [Income](script/notebook_python/income/income.ipynb) | Parse point amounts, ranges and upper or lower bounds, including K and M suffixes. | +83 pp (4% to 87%) | 14 to 6 formats. Free text was structured into numeric range minimum and maximum, less-than and greater-than thresholds, and point amounts, with unknown retained. |
| [Date Of Birth](script/notebook_python/date_of_birth/date_of_birth.ipynb) | Parse date patterns, convert Buddhist Era years and validate the resulting dates. | 0 pp (100% to 100%) | 50,255 to 50,168 distinct values. Dates were normalized to dd-mm-yyyy in the Common Era. |

The percentages show the share of known values in standard format before and after cleaning (Figure 9 of the report). Changes are in percentage points (pp). Table 12 rounds gender improvement to 100% and reports 0% for education, where there were no known values. Distinct counts also come from Table 12.

- [PySpark notebook](script/notebook_pyspark/DQ_improvement_public.ipynb)
- [Master dictionaries](dataset/master_dict/)
- [Cooperative education report (PDF)](report/Data%20quality%20improvement%20and%20examine%20the%20efficiency%20of%20demographic%20data%20for%20processing%20on%20cloud%20computing.pdf)
- [Project presentation (PowerPoint)](report/presentation.pptx)

## Output status

| Code | Label | Meaning |
| --- | --- | --- |
| `0` | Unhandled | The value could not be standardized. |
| `1` | Clean | The source value was already in standard format. |
| `2` | Improved | The value was successfully standardized. |
| `3` | NULL | The source value was missing. |

## Reported results

The internship report's Table 12 presents a change in standardized formats across seven evaluated attributes. It reports gender 100%, marital status 0%, education 0%, occupation 96%, nationality 100%, income 83% and date of birth 0% at the table's reported precision. These percentages use the report's definition and denominator. The report discusses known-value subsets separately.

## Data availability and reproduction

The folder includes dictionaries and notebooks. Input CSVs and the source dataset are unavailable here. The Python notebooks use pandas and local input paths from the original setup. To run a local copy, supply a CSV with the fields expected by the notebook, point the input and dictionary paths at your own files, and run the cells in order. The PySpark notebook requires a Spark environment and access to an S3 input you are authorized to use. Configure your own storage settings before running it.
