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
- Submission format: row_id, document, token, label
  - document: doc id
  - token: identifying token
  - label: BIO format with PII type
    - B-: beginning of PII entity
    - I-: continuation of PII entity
    - O-: not PII, exclude outer (O) labels  

## TODO
