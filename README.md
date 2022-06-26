# Lead scoring and segmentation for an online education company

- [Introduction](#introduction)
- [Objectives](#objectives)
- [Project structure](#project-structure)

## Introduction <a name="introduction"></a>
The client is an online education company which sells an online course to industry professionals.

The company markets their course on different websites and search engines. Once professionals who are interested in the course land on the website, they might browse the course or fill up a form for the course or watch some videos. When these people fill up a form providing their email address or phone number, they are classified to be a lead. Moreover, the company also gets leads through past referrals.

Once these leads are acquired, employees from the sales team start making calls, writing emails, etc. Through this process, some of the leads get converted while most do not, with the inefficiency of this process impacting company’s benefits.

## Objectives <a name="objectives"></a>
1. Analysing historical leads information to propose potential actions that increase overall company turnover.
2. Creating advanced analytical assets such as a predictive lead scoring and customer segmentation algorithms that helps sales team to identify both potential customers who are most likely to convert into paying customers and leads who are not economically profitable to manage.

## Project structure <a name="project-structure"></a>
- `01_Documents`
  - Contains basic project files:
    - *Leads Data Dictionary.pdf*: feature-level metadata.
    - *pf_leadscoring.yml*: project environment file.
    - *Development stage_Data Transformation Design.xlsx*: support file for designing feature transformation processes.
    - *Production stage_Processes Design*: support file for designing final production script.
- `02_Data`
  - `01_Originals`
    - *Leads.csv*: Original dataset.
  - `02_Validation`
    - *validation.csv*: Sample extracted from the original dataset at the beginning of the project in order to be used to check the correct performance of the model once it is put into production.
  - `03_Work`
    - This folder contains the datasets resulting from each of the stages of the project (data quality, exploratory data analysis, feature transformation...).
- `03_Notebooks`
  - `02_Development`
    - *00_Project Design.ipynb*:
    - *01_Set Up.ipynb*:
    - *02_Data Quality.ipynb*:
    - *03_EDA.ipynb*:
    - *04_Feature Transformation.ipynb*:
    - *05_Unsupervised Modelling.ipynb*:
    - *06_Feature Selection.ipynb*:
    - *07_Supervised Classification Modelling.ipynb*:
    - *08_Production Code Preparation.ipynb*:
    - *09_Retraining script.ipynb*:
    - *10_Execution script.ipynb*:
  - `03_System/App_lead_scoring`
    - This folder contains the files (app script, production script, models, ...) used in the deployment of the web application "Lead scoring analyzer".
- `04_Models`
  - *pipe_execution.pickle*: pipe that condenses the final trained model as well as all necessary prior data transformations.
  - *pipe_training.pickle*:  pipe that condenses the entire training process. It can be used to retrain the model with new data when necessary.
  - *optimal_disc_threshold.pickle*: Contains the value of the optimal discrimination threshold of the model that maximises the company's roi. It is used by *pipe_training.pickle* and is updated when re-training the model with *pipe_training.pickle*.
- `05_Results`
  - *Project Results.ipynb*: Notebook summarising the insights and KPIs improvements achieved from the exploratory data analysis as well as from the execution of the scoring and lead segmentation machine learning models.
  - *Execution script.py*: Python script to execute the model and obtain the results.
  - *Retraining script.py*: Python script to retrain the model with new data when necessary.
  - *final features.pickle*: Names of the final features pre-selected for input to the model.
