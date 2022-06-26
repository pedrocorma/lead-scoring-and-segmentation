#!/usr/bin/env python
# coding: utf-8

# # RETRAINING SCRIPT

# NOTE: This training code must be run using exactly the same environment in which it was created.
#
# The environment can be created using 'pf_leadscoring.yml' file which was created during the set up phase of the project. It can be found in the folder '01_Documents'.
#
# Copy 'pf_leadscoring.xml' file to the directory and using the terminal or anaconda prompt execute:
#
# conda env create --file pf_leadscoring.yml --name project_name

import numpy as np
import pandas as pd
import cloudpickle
from janitor import clean_names
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# Data importation
project_path = (r'C:\Users\pedro\PEDRO\DS\Portfolio\LEAD_SCORING').replace('\\','/')
data_file_name = 'Leads.csv'
full_path = project_path + '/02_Data/01_Originals/' + data_file_name
df = pd.read_csv(full_path,sep=',')

# Data quality
df = clean_names(df) \
       .rename(columns={'lead_number':'id',
                        'lead_source':'source',
                        'totalvisits':'total_visits',
                        'total_time_spent_on_website':'total_time_website',
                        'how_did_you_hear_about_x_education':'hear_about',
                        'what_is_your_current_occupation':'ocupation',
                        'what_matters_most_to_you_in_choosing_a_course':'matters_most',
                        'asymmetrique_activity_score':'activity_score',
                        'asymmetrique_profile_score':'profile_score',
                        'a_free_copy_of_mastering_the_interview':'lead_magnet'}) \
       .drop_duplicates() \
       .set_index('id')
df = df.loc[~((df.last_activity=='Email Bounced')|(df.last_notable_activity=='Email Bounced'))]

# Final features
final_features = ['activity_score',
                  'city',
                  'country',
                  'do_not_call',
                  'do_not_email',
                  'hear_about',
                  'last_activity',
                  'last_notable_activity',
                  'lead_magnet',
                  'lead_origin',
                  'matters_most',
                  'ocupation',
                  'page_views_per_visit',
                  'profile_score',
                  'source',
                  'specialization',
                  'total_time_website',
                  'total_visits']

# Final datasets
x = df[final_features].copy()

target = 'converted'
y = df[target].copy()

# Loading training pipe
name_pipe_training = 'pipe_training.pickle'
path_pipe_training = project_path + '/04_Models/' + name_pipe_training

with open(path_pipe_training, mode='rb') as file:
   pipe_training = cloudpickle.load(file)

# Retraining
pipe_execution = pipe_training.fit(x,y)

# Saving retrained execution pipe
name_pipe_execution = 'pipe_execution.pickle'
path_pipe_ejecucion = project_path + '/04_Models/' + name_pipe_execution

with open(path_pipe_ejecucion, mode='wb') as file:
   cloudpickle.dump(pipe_execution, file)

# Calculating optimal discrimination threshold
def disc_threshold_max_roi(y_true,y_scoring, itn, ifp, ifn, itp, step_size = 0.01):
    #Expected value function
    def expected_value(conf_matrix):
        tn, fp, fn, tp = conf_matrix.ravel()
        ev = (tn*itn) + (fp*ifp) + (fn*ifn) + (tp*itp)
        return(ev)

    #Expected value for each discrimination threshold
    ev_list = []
    for disc_threshold in np.arange(0,1,step_size):
        pred = np.where(y_scoring > disc_threshold,1,0)
        cm = confusion_matrix(y_true,pred)
        ev_list.append(tuple([disc_threshold,expected_value(cm)]))

    df_temp = pd.DataFrame(ev_list, columns=['discrimination_threshold','expected_value'])

    #Optimal values
    optimal_disc_threshold = df_temp.iloc[df_temp.expected_value.idxmax(),0]
    ev_max = df_temp.iloc[df_temp.expected_value.idxmax(),1]

    return(optimal_disc_threshold)

product_price = 49.99   # Product price
ltc_avg_cost = 3.25     # Lead-to-customer average cost

train_x,val_x,train_y,val_y = train_test_split(x,y,test_size=0.3)
threshold = pipe_training.fit(train_x,train_y)
pred_threshold = threshold.predict_proba(val_x)[:,1]

itn, ifp, ifn, itp = 0, -ltc_avg_cost, -product_price, product_price - ltc_avg_cost

optimal_disc_threshold = disc_threshold_max_roi(val_y,pred_threshold, itn, ifp, ifn, itp, step_size = 0.01)

# Saving optimal discrimination threshold
name_disc_threshold = 'optimal_disc_threshold.pickle'
path_disc_threshold = project_path + '/04_Models/' + name_disc_threshold

with open(path_disc_threshold, mode='wb') as file:
   cloudpickle.dump(optimal_disc_threshold, file)
