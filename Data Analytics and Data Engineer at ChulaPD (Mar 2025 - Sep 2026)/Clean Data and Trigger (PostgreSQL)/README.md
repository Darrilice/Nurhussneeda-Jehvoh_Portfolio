# Screening Assessment Data Cleaning and PostgreSQL Triggers

## Purpose

I preprocessed demographic and assessment data in Supabase so physicians and analysts could review consistent records. Duplicate submissions and incorrect or malformed assessment scores made patient records harder to review and could distort downstream score distributions.

## Assessment scope

| Domain | Assessments |
| --- | --- |
| Cognition | MoCA and TMSE |
| Mood and motor symptoms | HAM-D and MDS-UPDRS |
| Sleep | Epworth Sleepiness Scale and RBD Questionnaire |
| Smell and constipation | Thai Smell Identification Test and ROME IV |
| Diet and color vision | Thai MIND Diet Assessment and Farnsworth D-15 Color Vision |

## Workflow

1. **Check incoming records.** Review demographic fields, body measurements and assessment responses. Identify missing values, inconsistent formats, repeated records and invalid or unclear scores.
2. **Validate scores before analysis.** Check score formats and expected values against each instrument's reporting rules. Route scores that cannot be verified to review.
3. **Standardize and deduplicate.** Apply consistent formats and resolve duplicate records before preparing scores for comparison across PD, prodromal and control groups.
4. **Automate eligible checks.** Use SQL and PostgreSQL triggers on Supabase to apply cleaning rules when new records arrive. I also used SQL and Python for cross-checks across application and questionnaire data.

## Outcome

The workflow reduced duplicate records and helped catch score errors before the data reached clinical review or dashboards. Physicians had cleaner records to review, and analysts had more consistent inputs for score distributions. Clinical records and production SQL are held in the organizational system.
