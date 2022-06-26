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
# from janitor import clean_names

# Data importation
# project_path = (r'C:\Users\pedro\PEDRO\DS\Portfolio\LEAD_SCORING').replace('\\','/')
# data_file_name = 'validation.csv'
# full_path = project_path + '/02_Data/02_Validation/' + data_file_name
# df = pd.read_csv(full_path,sep=',')

# Data quality
# df = clean_names(df) \
#        .rename(columns={'lead_number':'id',
#                         'lead_source':'source',
#                         'totalvisits':'total_visits',
#                         'total_time_spent_on_website':'total_time_website',
#                         'how_did_you_hear_about_x_education':'hear_about',
#                         'what_is_your_current_occupation':'ocupation',
#                         'what_matters_most_to_you_in_choosing_a_course':'matters_most',
#                         'asymmetrique_activity_score':'activity_score',
#                         'asymmetrique_profile_score':'profile_score',
#                         'a_free_copy_of_mastering_the_interview':'lead_magnet'}) \
#        .drop_duplicates() \
#        .set_index('id')
# df = df.loc[~((df.last_activity=='Email Bounced')|(df.last_notable_activity=='Email Bounced'))]

# # Final features
# final_features = ['activity_score',
#                   'city',
#                   'country',
#                   'do_not_call',
#                   'do_not_email',
#                   'hear_about',
#                   'last_activity',
#                   'last_notable_activity',
#                   'lead_magnet',
#                   'lead_origin',
#                   'matters_most',
#                   'ocupation',
#                   'page_views_per_visit',
#                   'profile_score',
#                   'source',
#                   'specialization',
#                   'total_time_website',
#                   'total_visits']

# Final dataset
# df = df[final_features]

def run_model(df):
    # Loading execution pipe
    with open('pipe_execution.pickle', mode='rb') as file:
       pipe_execution = cloudpickle.load(file)

    # Loading optimal discrimination threshold
    with open('optimal_disc_threshold.pickle', mode='rb') as file:
       optimal_disc_threshold = cloudpickle.load(file)

    # Execution and results
    scoring = pipe_execution.predict_proba(df)[:, 1]
    manage_lead = where(scoring>optimal_disc_threshold, 'Yes', 'No')
    results = pd.DataFrame({'lead_score':round(scoring,2), 'manage_lead':manage_lead})

    return(results)
