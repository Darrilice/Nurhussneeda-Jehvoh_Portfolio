# Unhandled Values

## Purpose

I built a separate audit to show which nonblank laboratory and DTX result values could not be converted to numbers under the project parser. The detailed report helps locate a problematic record, while the grouped report helps prioritize recurring formats for review.

## Inputs and rules

The audit reads the raw LAB result field and raw DTX glucose field as text. It retains the original value for review and uses the applicable source date and patient key for internal traceability.

1. Check that the expected fields exist in both inputs.
2. Trim surrounding whitespace and identify blanks and configured missing markers such as `NA`, `NULL` and `NONE`.
3. Try numeric conversion on the remaining values. For DTX, a project-specific rule accepts two valid numbers separated by a single slash, averages them and rounds to three decimals. For example, fictional input `120/124` produces `122.000`.
4. Log the nonblank values that still fail conversion. Record the source table, field, original text, reason and traceability fields in the internal exception detail.
5. Group the exceptions by source and original value, then count how often each occurs. Keep the exception outputs separate from the main cleaning exports.

## Results and handover

The documented run flagged **58,943 rows across 14 distinct value groups**. All flagged rows came from the LAB result field. No DTX rows were flagged by this parser in that run. The totals describe numeric parsing coverage. Other DTX quality checks, such as range or date validation, are handled in the main pipeline.

The handover included two CSVs, one for record-level review and one for grouped counts, plus metadata describing the outputs. The audit leaves the source extracts and main pipeline outputs intact.

### **-- Skills and tools --**
#### Python, Jupyter, numeric parsing, missing-value handling, exception reporting, frequency analysis and data quality auditing.
