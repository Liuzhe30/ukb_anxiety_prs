import pandas as pd
import numpy as np

score_dict = {"1":1, "2":2, "3":3}
id_list = ['20506', '20509', '20520', '20515', '20516', '20505', '20512']
path = 'GAD-7-sample-id/'
sample_dict = {}

for gad in id_list:
    csv1 = pd.read_csv(path + gad + '-1.csv')
    #print(csv1['eid'])
    for item in csv1['eid']:
        sample_id = str(item)
        if(sample_id not in sample_dict.keys()):
            sample_dict[sample_id] = 1
        else:
            sample_dict[sample_id] += 1
    
    
    csv2 = pd.read_csv(path + gad + '-2.csv')
    #print(csv2['Participant ID'])
    for item in csv2['Participant ID']:
        sample_id = str(item)
        if(sample_id not in sample_dict.keys()):
            sample_dict[sample_id] = 2
        else:
            sample_dict[sample_id] += 2    
            
    csv3 = pd.read_csv(path + gad + '-3.csv')
    #print(csv3['Participant ID'])
    for item in csv3['Participant ID']:
        sample_id = str(item)
        if(sample_id not in sample_dict.keys()):
            sample_dict[sample_id] = 3
        else:
            sample_dict[sample_id] += 3

# check score >= 10
count_case = 0
case_list = []
for key in sample_dict.keys():
    if(sample_dict[key] >= 5):
        count_case += 1
        case_list.append(key)
case_numpy = np.array(case_list)
np.savetxt('case_id_gad5.txt', case_numpy, fmt='%s')
print(count_case)
    