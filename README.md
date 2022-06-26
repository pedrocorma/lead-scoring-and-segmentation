# Lead scoring and segmentation for an online education company

- [Introduction](#introduction)
- [Objectives](#objectives)
- [Project results](#project-results)
- [Project structure](#project-structure)
- [Instructions](#project-instructions)
- [License](#licensing)

## Introduction <a name="introduction"></a>
The client is an online education company which sells an online course to industry professionals.

The company markets their course on different websites and search engines. Once professionals who are interested in the course land on the website, they might browse the course or fill up a form for the course or watch some videos. When these people fill up a form providing their email address or phone number, they are classified to be a lead. Moreover, the company also gets leads through past referrals.

Once these leads are acquired, employees from the sales team start making calls, writing emails, etc. Through this process, some of the leads get converted while most do not, with the inefficiency of this process impacting company’s benefits.

## Objectives <a name="objectives"></a>
1. Analysing historical leads information to propose potential actions that increase overall company turnover.
2. Creating advanced analytical assets such as a predictive lead scoring and customer segmentation algorithms that helps sales team to identify both potential customers who are most likely to convert into paying customers and leads who are not economically profitable to manage.

## Project results  <a name="project-results"></a>


## Project structure <a name="project-structure"></a>
- :file_folder: 01_Documents
  - Contains basic project files:
    - `Leads Data Dictionary.pdf`: feature-level metadata.
    - `pf_leadscoring.yml`: project environment file.
    - `Development stage_Data Transformation Design.xlsx`: support file for designing feature transformation processes.
    - `Production stage_Processes Design`: support file for designing final production script.
- :file_folder: 02_Data
  - :file_folder: 01_Originals
    - `Leads.csv`: Original dataset.
  - :file_folder: 02_Validation
    - `validation.csv`: Sample extracted from the original dataset at the beginning of the project in order to be used to check the correct performance of the model once it is put into production.
  - :file_folder: 03_Work
    - This folder contains the datasets resulting from each of the stages of the project (data quality, exploratory data analysis, feature transformation...).
- :file_folder: 03_Notebooks
  - :file_folder: 02_Development
    - `00_Project Design.ipynb`: Notebook compiling the initial design of the project.
    - `01_Set Up.ipynb`: Notebook used for the initial set up of the project.
    - `02_Data Quality.ipynb`: Notebook detailing and executing all data quality processes.
    - `03_EDA.ipynb`: Notebook used for the execution of the exploratory data analysis and which collects the business insights found.
    - `04_Feature Transformation.ipynb`: Notebook that details and executes the data transformation processes necessary to prepare the features  for input into the models.
    - `05_Unsupervised Modelling.ipynb`: Notebook for modelling the unsupervised Kmeans algorithm used to perform lead segmentation. It also includes the segment profiling from a business point of view as well as the insights and conclusions obtained from this process.
    - `06_Feature Selection.ipynb`: Notebook used to make a selection of the final variables to be entered into the models.
    - `07_Supervised Classification Modelling.ipynb`: Notebook for modelling the predictive lead scoring model. Model selection, hyperparameterisation, selection of the optimal discrimination threshold and evaluation of results.
    - `08_Production Code Preparation.ipynb`: Notebook used to compile all the quality, transformation and variable selection processes, as well as the final model and execution and retraining processes, with the aim of creating the final retraining and execution pipes that condense all the aforementioned processes.
    - `09_Retraining script.ipynb`: Notebook to retrain the model with new data when necessary.
    - `10_Execution script.ipynb`: Notebook to execute the final model and obtain the results.
  - :file_folder: 03_System/App_lead_scoring
    - This folder contains the files (app script, production script, models, ...) used in the deployment of the web application [Lead scoring analyzer"](https://p-03-notebooks03-systemapp-lead-scoringapp-lead-scoring-asrw2z.streamlitapp.com/).
- :file_folder: 04_Models
  - `pipe_execution.pickle`: pipe that condenses the final trained model as well as all necessary prior data transformations.
  - `pipe_training.pickle`:  pipe that condenses the entire training process. It can be used to retrain the model with new data when necessary.
  - `optimal_disc_threshold.pickle`: Contains the value of the optimal discrimination threshold of the model that maximises the company's roi. It is used by *pipe_training.pickle* and is updated when re-training the model with *pipe_training.pickle*.
- :file_folder: 05_Results
  - `Project Results.ipynb`: Notebook summarising the insights and KPIs improvements achieved from the exploratory data analysis as well as from the execution of the scoring and lead segmentation machine learning models.
  - `Execution script.py`: Python script to execute the model and obtain the results.
  - `Retraining script.py`: Python script to retrain the model with new data when necessary.
  - `final features.pickle`: Names of the final features pre-selected for input to the model.

## Instructions  <a name="instructions"></a>
The project should be run using exactly the same environment in which it was created.

- Project environment can be replicated using 'pf_leadscoring.yml' file which was created during the set up phase of the project. It can be found in the folder '01_Documents'.
- Copy 'pf_leadscoring.yml' file to the directory and using the terminal or anaconda prompt execute:
    > conda env create --file pf_leadscoring.yml --name project_name

By other hand, remember to update the `project_path` variable of the notebooks to the path where you have replicated the project.

## Licensing <a name="licensing"></a>
The data set, licensing, and other descriptive information is available [here](https://www.kaggle.com/code/ashydv/lead-scoring-logistic-regression).
