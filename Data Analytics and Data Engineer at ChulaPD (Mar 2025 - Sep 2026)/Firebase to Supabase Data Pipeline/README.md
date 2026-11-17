# Firebase to Supabase Data Pipeline and Storage Quality

## Weekly delivery and reconciliation

The team moved JSON and WAV files from Firebase Storage to Supabase buckets on a weekly schedule, with GCP/Cloud Run supporting scheduled ingestion. The workflow standardized file organization and classified records into PD, control and prodromal groups.

I performed the final destination checks in Supabase. I compared the delivered files and participant inventory with the source, identified missing records or test modalities, and verified that the data matched what was expected. Weekly automated delivery reduced manual backup work, made files easier to find and reduced opportunities for manual errors.

## Storage checks and data utilities

I supported separate biweekly sample checks to verify that expected files in Supabase Storage were present and readable. Firebase tools located records from authorized input lists, checked file availability and retrieved matching JSON or WAV files for analysis.
