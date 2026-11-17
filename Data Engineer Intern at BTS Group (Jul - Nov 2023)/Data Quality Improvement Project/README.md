# Data Quality Improvement Project

## Objective

This project standardized self-entered demographic values for downstream analysis. I profiled recurring input patterns, defined a standard format for each field, and developed rules to transform usable values and flag unresolved cases.

The internship report covers 14 attributes. The seven fields evaluated on the actual dataset were gender, marital status, education, occupation, nationality, income, and date of birth. The report also documents work on email, phone number, language, ID card, passport number, address, and name.

## Workflow

1. **Profile the sample dataset.**
    - Review distinct formats, missing values, malformed entries, and recurring variants.
2. **Define field-level standards.**
    - Use regular expressions, lookup dictionaries, fuzzy matching, and field-specific validation as appropriate.
3. **Develop and test the Python functions on the sample dataset.**
    - Compare representative inputs with expected outputs and inspect the `status` assigned to each value.
4. **Run PySpark on the actual dataset.**
    - Read data from Amazon S3 and process it on Amazon EMR. Compare the share of known values in standard format and examine changes in the number of distinct formats or values.

## Python notebooks and actual dataset results

The linked Python notebooks show the rules developed and tested using the **sample dataset**. The results in the last two columns come from the **actual dataset** evaluated with PySpark.

| Field and Python notebook | Method | Standardization improvement on actual data | What changed on actual data |
| --- | --- | --- | --- |
| [Gender](script/notebook_python/gender/gender.ipynb) | Normalize Thai and English labels into standard categories. | 0.023% → 100% (approximately +100 pp) | 9 → 3 formats. Variants were consolidated into male, female, and unknown. |
| [Marital Status](script/notebook_python/marital_status/marital_status.ipynb) | Map Thai and English marital-status variants. | Before-and-after rate unverified | 5 → 4 formats. Married, widowed, and single were retained, and unresolved variants were grouped as unknown. |
| [Education](script/notebook_python/education/education.ipynb) | Map recognized abbreviations and labels by education level. | Rate unavailable because there were no known values | 1 → 1 format. The evaluated field remained unknown. |
| [Occupation](script/notebook_python/occupation/occupation.ipynb) | Standardize role and employment descriptions with text rules and mappings. | 4% → 100% (+96 pp) | 19 → 18 formats. Role and employment variants were mapped to standard categories, with unknown retained. |
| [Nationality](script/notebook_python/nationality/nationality.ipynb) | Normalize country codes and compare unmatched names with dictionary entries. | 0% → 100% (+100 pp) | 2 → 2 formats. The output categories were Thai and unknown. |
| [Income](script/notebook_python/income/income.ipynb) | Parse point amounts, ranges, and thresholds, including K and M suffixes. | 4% → 87% (+83 pp) | 14 → 6 formats. Free text was structured into numeric range minimums and maximums, less-than and greater-than thresholds, and point amounts, with unknown retained. |
| [Date of Birth](script/notebook_python/date_of_birth/date_of_birth.ipynb) | Parse date patterns, convert Buddhist Era years, and validate the resulting dates. | Before-and-after rate unverified | 50,255 → 50,168 distinct values. Dates were normalized to `dd-mm-yyyy` in the Common Era. |

The percentages are the shares of **known values** in standard format reported in Figure 9. Changes are expressed in percentage points (pp). The distinct counts come from Table 12. Figure 9 gives before-and-after rates for marital status and date of birth that the report does not reconcile with Table 11. The table therefore cites the documented format or value counts for those two fields.

## Output status

| Code | Label | Meaning |
| --- | --- | --- |
| `0` | Unhandled | The value could not be standardized. |
| `1` | Clean | The source value was already in standard format. |
| `2` | Improved | The value was successfully standardized. |
| `3` | NULL | The source value was missing. |

## Data availability and reproduction

The portfolio includes notebooks and lookup dictionaries. The original sample CSVs and actual dataset are unavailable here.

To run a Python notebook locally, supply your own CSV with the columns expected by the notebook and update its input and dictionary paths before running the cells. To run the PySpark notebook, configure a Spark environment and an S3 input you are authorized to use.

## Project materials

- [PySpark notebook](script/notebook_pyspark/DQ_improvement_public.ipynb)
- [Master dictionaries](dataset/master_dict/)
- [Cooperative education report (PDF)](report/Data%20quality%20improvement%20and%20examine%20the%20efficiency%20of%20demographic%20data%20for%20processing%20on%20cloud%20computing.pdf)
- [Project presentation (PowerPoint)](report/presentation.pptx)
