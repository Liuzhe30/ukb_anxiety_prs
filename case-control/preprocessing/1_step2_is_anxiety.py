import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
import warnings

warnings.filterwarnings('ignore')

# case ids
case_list = []
with open('case_id_gad5.txt') as case_file:
    line = case_file.readline()
    while line:
        case = str(line.strip())
        case_list.append(case)
        line = case_file.readline()
#print(case_list)

# control ids
control_list = []
with open('control_id_gad5.txt') as control_file:
    line = control_file.readline()
    while line:
        control = str(line.strip())
        control_list.append(control)
        line = control_file.readline()
#print(control_list)

# full table
data = pd.read_csv('covariables/1_cov_phe_merge.csv')
first_rows = data.head(5)
print(first_rows)
print(len(data))

data_new = pd.DataFrame()
for i in range(len(data)):
    FID = str(data['FID'][i])
    # if(FID not in case_list and FID not in control_list):
    #     data = data[~data['FID'].isin([FID])] 
    if(FID in case_list):
        row_data = data.iloc[[i]]
        row_data['Is_anxiety'][i] = 1
        row_data['Is_anxiety'] = row_data['Is_anxiety'].astype(int)
        row_data.fillna('NA', inplace = True)
        data_new = pd.concat([data_new, row_data], axis = 0)
    elif(FID in control_list):
        row_data = data.iloc[[i]]
        row_data['Is_anxiety'][i] = 0
        row_data['Is_anxiety'] = row_data['Is_anxiety'].astype(int)
        row_data.fillna('NA', inplace = True)
        data_new = pd.concat([data_new, row_data], axis = 0)
    print(len(data_new))
    data_new.to_csv('covariables/2_is_anxiety.csv')

data_new = data_new.reset_index(drop=True)   
print(data_new)     
print(len(data_new))

# save
data_new.to_csv('covariables/2_is_anxiety.csv')