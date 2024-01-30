# Requirements
## Summary
The goal of this competition is to develop a model that detects sensitive personally identifiable information (PII) in student writing. This is necessary to screen and clean educational data so that when released to the public for analysis and archival, the students' risk are mitigated.
## User Requirements
- Given a test and training dataset, identify 7 types of PII
  - NAME_STUDENT - full or partial, not necessarily the author of the essay, excludes other persons names
  - EMAIL
  - USERNAME - username on any platform.
  - ID_NUM - number or sequence of characters used to identify a student
  - PHONE_NUM - associated with a student.
  - URL_PERSONAL
  - STREET_ADDRESS - full or partial street address
- Hard Deadlines
  - 04/16/2024 - Entry Deadline
  - 04/23/2024 - Final Submission Deadline
- Functional Requirements
  - CPU Notebook <= 9 hours run-time
  - GPU Notebook <= 9 hours run-time
  - Internet access disabled
  - Publicly available external data allowed
  - Final file: submission.csv
- Should match with given submission_sample.csv
  - Evaluation score > 0.8?, > 50 percentile
- Simple website with team info, visualizations, description, procedures and algorithms

## Systems Requirements
- Submission format: row_id, document, token, label
  - Document: doc id
  - Token: identifying token
  - Label: BIO format with PII type
    - B-: beginning of PII entity
    - I-: continuation of PII entity
    - O-: not PII, exclude outer (O) labels
- Read through tokens/document
  - Pandas
  - JSON module
- Identify which category each token falls under as a token label
  - Identify the context of each token
    - Use the surrounding tokens to identify competition
    - Identify usage of whitespace as context
- Identify BIO for each token label
  - Identify the context of each token
  - Use context to add BIO label
  - Identify usage of whitespace as context
  - Filter out O- token labels
- External datasets
  - Collect
  - Munge
  - Add to training data
- 2-3 data visualization for presentations
  - Analytics of PII distribution
    - Length vs amount using linear regression
  - Software
    - Power BI
    - Matplotlib
    - R
- Webpage
  - markdown gist, include:
    - team info
    - visualizations
    - project description
    - procedure
    - algorithms


## Deliverables
- 1st iteration
  - Data collection
    - Kaggle test/training
    - External data for after 1st model
    - Mock up of webpage
- 2nd iteration
  - Initial data exploration using test dataset (priority)
  - 1st model from training dataset
    - Find ML python library
  - 1st evaluation
  - Wireframe of results webpage
- 3rd iteration
  - Visualizations
  - Iterate model with optimizations
  - Iterate model using external datasets
  - 2nd evaluation
  - Post results webpage
    - AWS EC2
