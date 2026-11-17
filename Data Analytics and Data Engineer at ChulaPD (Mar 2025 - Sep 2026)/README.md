# Data Analyst & Data Engineer at ChulaPD (Mar 2025 - Sep 2026)

At ChulaPD, I worked on CheckPD, a digital Parkinson's screening programme, and on the team's Screening Assessments data. My work covered reporting for executives and project coordinators, quality checks for clinical and application data, and preparation of motion-sensor features for researchers and data scientists.

## Projects at a glance

| Project | Main contribution | Key skills |
| --- | --- | --- |
| [Dashboard](#checkpd-and-screening-assessments-dashboards) | Built six dashboards for app usage, screening completion and follow-up. | Looker Studio, KPI definition, completion analysis |
| [Screening Data Cleaning](#screening-data-cleaning-and-postgresql-triggers) | Validated assessment scores and automated cleaning for incoming records. | SQL, PostgreSQL triggers, Supabase, data validation |
| [Sensor Feature Extraction](#sensor-feature-extraction-and-validation) | Extracted motion features and evaluated their reliability. | Python, signal processing, feature engineering |
| [Firebase to Supabase Pipeline](#firebase-to-supabase-data-pipeline-and-storage-quality) | Reconciled weekly file deliveries and checked storage quality. | Firebase, Supabase, file reconciliation |
| [Field Collection and Usability](#field-data-collection-usability-testing-and-ux-requirements) | Collected screening data and translated usability feedback into app requirements. | Field data collection, usability testing, requirements gathering |
| [Data Architecture and Documentation](#data-architecture-and-documentation) | Documented data flows, table relationships and field definitions. | Data flow diagrams, ERDs, data dictionaries |
| [Research and Publication](#research-and-publication) | Co-authored a peer-reviewed study on CheckPD adoption and performance. | Research collaboration, dataset preparation, research reporting |

## [CheckPD and Screening Assessments Dashboards](Dashboard/README.md)

I gathered requirements from executives and project coordinators and built, maintained and revised six dashboards in Google Data Studio (Looker Studio). The views tracked app usage by province and time, showed where users stopped during screening, and compared app risk classifications with physician follow-up where available. I also built views for exploring assessment score distributions across PD, prodromal and control groups.

The team used completion reporting and field observations to understand barriers such as difficult tests and confusing instructions. After the app update, the dashboard showed a higher share of users completing the required tests. The release changed which tests were required, so the comparison used each period's test battery.

### **-- Skills and tools --**
#### Stakeholder interviews, KPI definition, dashboard design, cohort and completion analysis, data visualization, Looker Studio and Python.

## [Screening Data Cleaning and PostgreSQL Triggers](Clean%20Data%20and%20Trigger%20%28PostgreSQL%29/README.md)

I preprocessed demographic data, body measurements and scores from 10 screening assessments, including MoCA, HAM-D and MDS-UPDRS. I checked for missing values, invalid scores, inconsistent formats and duplicate records before the data went into clinical review and score-distribution reporting. I wrote PostgreSQL triggers in Supabase to apply eligible cleaning rules as new records arrived.

### **-- Skills and tools --**
#### SQL, PostgreSQL triggers, Supabase, Python, data profiling, score validation, deduplication and data quality checks across sources.

## [Sensor Feature Extraction and Validation](Sensor%20Feature%20Extraction%20%28Python%29/README.md)

I built a Python workflow that turned six-axis smartphone recordings into numeric features for resting tremor, postural tremor, standing balance and walking. The workflow retained 952 of 1,000 sampled participant records and defined 715 candidate features. I produced feature tables, dictionaries and quality reports for downstream research and model development.

I compared full and curated feature sets, examined clusters within the reference cohort and tested feature reliability at the observed recording duration of about 20 seconds. Standing balance showed the clearest cluster separation and the lowest estimated reliability at that duration.

### **-- Skills and tools --**
#### Python, time-series preprocessing, signal filtering and resampling, Welch spectral analysis, feature engineering, outlier detection, PCA, clustering and split-half reliability.

## [Firebase to Supabase Data Pipeline and Storage Quality](Firebase%20to%20Supabase%20Data%20Pipeline/README.md)

I verified the weekly delivery of JSON and WAV files from Firebase Storage to Supabase. I reconciled the destination inventory with the source and identified missing participant records or test files. I also supported biweekly storage sampling and used file retrieval tools to locate recordings for authorized analyses.

### **-- Skills and tools --**
#### File inventory reconciliation, completeness checks, storage quality sampling, JSON and WAV file handling, Firebase Storage and Supabase Storage. The team's scheduled ingestion workflow used GCP and Cloud Run.

## [Field Data Collection, Usability Testing and UX Requirements](Field%20Data%20Collection%20and%20Usability%20Testing/README.md)

I supported field collection across provinces for voice, tremor, finger tapping, gait, balance and risk questionnaires. I tested the app and shared observations about barriers that older users faced. I also gathered requirements from nutrition, exercise and sleep teams and worked with UX/UI designers to turn them into app flows.

### **-- Skills --**
#### Field data collection, usability testing, qualitative feedback synthesis, requirements gathering and cross-functional collaboration.

## [Data Architecture and Documentation](Data%20Architecture%20and%20Documentation/README.md)

I created and maintained data flow diagrams, entity relationship diagrams and a data dictionary for CheckPD and Screening Assessments. The documents traced how data moved from collection to storage and reporting, showed how tables related, and recorded field definitions, sources, types and privacy levels for validation and handover.

### **-- Skills --**
#### Data flow mapping, relational data modeling, ERD design, metadata documentation and technical handover.

## [Research and Publication](Research%20and%20Publication/README.md)

I co-authored a peer-reviewed study on the reach, adoption and real-world performance of CheckPD in Thailand, published in *BMC Public Health* in May 2026. The project materials include dataset preparation, demographic encoding, tables, figures and workflow diagrams that supported the manuscript. The linked project page provides the publication and its reported findings.

### **-- Skills --**
#### Research collaboration, dataset preparation, demographic encoding, and preparation of research tables and figures.
