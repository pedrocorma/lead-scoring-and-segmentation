#!/usr/bin/env python
# coding: utf-8

# # EXECUTION SCRIPT

# NOTE: This training code must be run using exactly the same environment in which it was created.
#
# The environment can be created using 'pf_leadscoring.yml' file which was created during the set up phase of the project. It can be found in the folder '01_Documents'.
#
# Copy 'pf_leadscoring.xml' file to the directory and using the terminal or anaconda prompt execute:
#
# conda env create --file pf_leadscoring.yml --name project_name

import cloudpickle
import pandas as pd
from numpy import where, round

def run_model(df):
    # Loading execution pipe
    with open('03_Notebooks/03_System/App_lead_scoring/pipe_execution.pickle', mode='rb') as file:
       pipe_execution = cloudpickle.load(file)

    # Loading optimal discrimination threshold
    with open('03_Notebooks/03_System/App_lead_scoring/optimal_disc_threshold.pickle', mode='rb') as file:
       optimal_disc_threshold = cloudpickle.load(file)

    # Execution and results
    scoring = pipe_execution.predict_proba(df)[:, 1]
    manage_lead = where(scoring>optimal_disc_threshold, 'Yes', 'No')
    results = pd.DataFrame({'lead_score':round(scoring,2), 'manage_lead':manage_lead})

    return(results)
