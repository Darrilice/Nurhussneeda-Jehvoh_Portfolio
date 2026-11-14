# Facebook Live sellers in Thailand

**Year 2 · Database Systems for Data Science · MySQL, SQL aggregation**

## Primary evidence and code status

The [original report](report/Facebook%20Live%20Sellers%20in%20Thailand%20Data%20Set.pdf) and `result/capture/` screenshots document the analysis. Original runnable SQL was not recovered. `script/analysis.sql` is a later reconstruction, not the submitted code.

## Dataset and workflow

`dataset/live2.csv` has **7,050 posts and 12 fields** covering post type, publication time, reactions, comments and shares. The report describes MySQL aggregation, `DISTINCT`, `ORDER BY`, `GROUP BY` and subqueries.

## End-to-end workflow

The documented sequence is: inspect the CSV → query engagement by post type in MySQL → compare counts and interactions → present the findings in the report. The exact original queries cannot be rerun from the surviving files.

## Results and outcome

Photos averaged **178.78 likes**; videos had **269,997 total shares**. The CSV has 7,050 data rows, while the report states 7,051 instances.

## Saved historical results

The report and `result/capture/` hold original outputs. `result/status-type-summary.csv` was recalculated later from the CSV and is labelled separately.

## Files

[`dataset/live2.csv`](dataset/live2.csv) · [`script/analysis.sql`](script/analysis.sql) · [`result/`](result/) · [`report/`](report/)
