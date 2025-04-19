MIMIC-III 的数据训练了个ML Disease Prediction Model

EHR-based prediction


MIMIC-III dataset MIMIC-III (Medical Information Mart for Intensive Care) is a publicly available database containing deidentified health-related data for ICU patients. This database consists of 26 tables and includes information about over forty thousand patients who stayed in critical care units at the Beth Israel Deaconess Medical Center between 2001 and 2012. The data encompasses demographics, laboratory test results, procedures, medications, caregiver notes, and imaging reports.

Tables Related to Patient Stays: ADMISSIONS: Every unique hospitalization for each patient in the database (defines HADM_ID) CALLOUT: Information regarding when a patient was cleared for ICU discharge and when the patient was actually discharged ICUSTAYS: Every unique ICU stay in the database (defines ICUSTAY_ID) PATIENTS: Every unique patient in the database (defines SUBJECT_ID) SERVICES: The clinical service under which a patient is registered TRANSFERS: Patient movement from bed to bed within the hospital, including ICU admission and discharge Tables Containing Critical Care Unit Data: CAREGIVERS: Every caregiver who has recorded data in the database (defines CGID) CHARTEVENTS: All charted observations for patients DATETIMEEVENTS: All recorded observations which are dates, for example ti## MIMIC-III dataset MIMIC-III (Medical Information Mart for Intensive Care) is a publicly available database containing deidentified health-related data for ICU patients. This database consists of 26 tables and includes information about over forty thousand patients who stayed in critical care units at the Beth Israel Deaconess Medical Center between 2001 and 2012. The data encompasses demographics, laboratory test results, procedures, medications, caregiver notes, and imaging reports.

Tables Related to Patient Stays:
ADMISSIONS: Every unique hospitalization for each patient in the database (defines HADM_ID)
CALLOUT: Information regarding when a patient was cleared for ICU discharge and when the patient was actually discharged
ICUSTAYS: Every unique ICU stay in the database (defines ICUSTAY_ID)
PATIENTS: Every unique patient in the database (defines SUBJECT_ID)
SERVICES: The clinical service under which a patient is registered
TRANSFERS: Patient movement from bed to bed within the hospital, including ICU admission and discharge
Tables Containing Critical Care Unit Data:
CAREGIVERS: Every caregiver who has recorded data in the database (defines CGID)
CHARTEVENTS: All charted observations for patients
DATETIMEEVENTS: All recorded observations which are dates, for example time of dialysis or insertion of lines
INPUTEVENTS_CV: Intake for patients monitored using the Philips CareVue system while in the ICU
INPUTEVENTS_MV: Intake for patients monitored using the iMDSoft Metavision system while in the ICU
NOTEEVENTS: Deidentified notes, including nursing and physician notes, ECG reports, imaging reports, and discharge summaries
OUTPUTEVENTS: Output information for patients while in the ICU
PROCEDUREEVENTS_MV: Patient procedures for the subset of patients who were monitored in the ICU using the iMDSoft MetaVision system
Tables Related to Hospital Record Systems:
CPTEVENTS: Procedures recorded as Current Procedural Terminology (CPT) codes
DIAGNOSES_ICD: Hospital assigned diagnoses, coded using the International Statistical Classification of Diseases and Related Health Problems (ICD) system
DRGCODES: Diagnosis Related Groups (DRG), which are used by the hospital for billing purposes
LABEVENTS: Laboratory measurements for patients both within the hospital and in outpatient clinics
MICROBIOLOGYEVENTS: Microbiology measurements and sensitivities from the hospital database
PRESCRIPTIONS: Medications ordered, and not necessarily administered, for a given patient
PROCEDURES_ICD: Patient procedures, coded using the International Statistical Classification of Diseases and Related Health Problems (ICD) system
Dictionary Tables:
D_CPT: High-level dictionary of Current Procedural Terminology (CPT) codes
D_ICD_DIAGNOSES: Dictionary of International Statistical Classification of Diseases and Related Health Problems (ICD) codes relating to diagnoses
D_ICD_PROCEDURES: Dictionary of International Statistical Classification of Diseases and Related Health Problems (ICD) codes relating to procedures
D_ITEMS: Dictionary of ITEMIDs appearing in the MIMIC database, except those that relate to laboratory tests
D_LABITEMS: Dictionary of ITEMIDs in the laboratory database that relate to laboratory tests
Data Extraction for 10,000 Patients
To extract data at the patient level, two datasets are created for each table based on unique identifier, SUBJECT_ID.

Creating Two Datasets:

First 10,000 SUBJECT_IDs: ‘TABLE_sorted.csv’
Random 10,000 SUBJECT_IDs: ‘TABLE_random.csv’


> https://physionet.org/content/mimiciii/1.4/

> https://github.com/MIT-LCP/mimic-code/

> https://www.kaggle.com/code/yilliee/mimic-iii-notebook-summer/notebook

> https://www.kaggle.com/code/mvanshika/diabetes-prediction#9.4-Decision-Tree

> https://www.kaggle.com/code/iamleonie/wids-datathon-2021-diabetes-detection

https://www.kaggle.com/code/shrutimechlearn/step-by-step-diabetes-classification

https://www.kaggle.com/code/mvanshika/diabetes-prediction

https://www.kaggle.com/code/nancyalaswad90/diabetes-database

https://www.kaggle.com/code/vincentlugat/pima-indians-diabetes-eda-prediction-0-906

https://www.kaggle.com/code/ohseokkim/diabetes-three-ensemble-models#Comparing-Models

https://www.kaggle.com/code/melikedilekci/diabetes-dataset-for-beginners

https://www.kaggle.com/code/paultimothymooney/predict-diabetes-from-medical-records

https://www.kaggle.com/code/zabihullah18/diabetes-prediction

https://www.kaggle.com/code/imtkaggleteam/diabetes-analysis

https://www.kaggle.com/code/aryantiwari123/diabetes-prediction-eda-10-models#10.-ExtraTreesClassifier
