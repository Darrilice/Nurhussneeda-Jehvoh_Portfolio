# Data Engineer Intern at BTS Group (July to November 2023) - Cooperative education

## Project objective

BTS Group collected self-entered demographic data in multiple formats. Differences in spelling, abbreviations, units and date conventions made the fields harder to group and analyze. I developed rules for 14 attributes to convert usable values into consistent formats, flag values that needed review, and prepare the workflow for distributed processing on AWS.

## How I did it

1. **Profiled the inputs.**
     - Reviewed representative values and grouped recurring issues such as spelling variants, incomplete entries, mixed income formats and inconsistent date conventions.
2. **Defined the standard for each field.**
     - Used regular expressions and dictionaries to normalize text, fuzzy matching for nationality variants, and date parsing to convert Buddhist Era dates where applicable. For income, separated point amounts, ranges, and upper or lower thresholds into numeric outputs.
3. **Built and tested Python functions on a sample dataset.**
    - Used representative records to test each field’s rules and compare the outputs with expected results. The status column identified values that were already in standard format, successfully standardized, unhandled, or missing.
4. **Processed and evaluated the actual dataset with PySpark.**
    - Adapted the Python rules for distributed processing on Amazon EMR, using data stored in Amazon S3 and compared the share of known values in standard format before and after processing and checked how the number of distinct formats or values changed across seven fields.

## Results (Actual Dataset)

| Field | Standardized share among known values | What changed |
| --- | --- | --- |
| Gender | 0.023% to 100% | Nine formats consolidated into three categories, including unknown. |
| Occupation | 4% to 100% | Role and employment variants mapped to standardized categories. |
| Nationality | 0% to 100% | The evaluated outputs resolved to Thai and unknown. |
| Income | 4% to 87% | Free text was structured into numeric amounts, ranges and thresholds. |

Marital status and date of birth stayed at 100% on the same known-value measure. Marital-status formats decreased from five to four, and distinct date-of-birth values decreased from 50,255 to 50,168 after normalization. The evaluated data contained no known education values.

The project delivered field-specific Python rules, a PySpark notebook, lookup dictionaries and a before-and-after evaluation. The portfolio includes seven Python notebooks and the project documentation. The original dataset is unavailable here.

## Project materials

- [Detailed project README and notebook index](Data%20Quality%20Improvement%20Project/README.md)
- [Cooperative education report (PDF)](Data%20Quality%20Improvement%20Project/report/Data%20quality%20improvement%20and%20examine%20the%20efficiency%20of%20demographic%20data%20for%20processing%20on%20cloud%20computing.pdf)
- [Project presentation (PowerPoint)](Data%20Quality%20Improvement%20Project/report/presentation.pptx)
