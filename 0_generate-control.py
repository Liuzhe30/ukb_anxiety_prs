import pandas as pd
import numpy as np
path = 'non-control/'

list_all = []
list_icd10_IV = []
list_icd10_V = []
list_drug = []
list_doctor = []
list_case = []
list_control = []


# all
data = pd.read_csv(path + 'all.csv')
for eid in data['eid']:
    list_all.append(int(eid))
print("count all: " + str(len(list_all)))

# icd10_IV
data = pd.read_csv(path + 'ICD10-IV.csv')
for eid in data['eid']:
    list_icd10_IV.append(int(eid))
print("count icd10_IV: " + str(len(list_icd10_IV)))

# icd10_V
data = pd.read_csv(path + 'ICD10-V.csv')
for eid in data['eid']:
    list_icd10_V.append(int(eid))
print("count icd10_V: " + str(len(list_icd10_V)))
    
# doctor
data = pd.read_csv(path + 'doctor.csv')
for eid in data['eid']:
    list_doctor.append(int(eid))
print("count mental distress: " + str(len(list_doctor)))
    
# drug
data = pd.read_csv(path + 'drug.csv')
for eid in data['Participant ID']:
    list_drug.append(int(eid))
print("count psychotic experience: " + str(len(list_drug)))
    
# case
with open("case_id_gad5.txt") as file:
    line = file.readline()
    while line:
        list_case.append(int(line.strip()))
        line = file.readline()
print("count case: " + str(len(list_case)))

idx = 1
for part in list_all:
    if((part not in list_icd10_IV) and
       (part not in list_icd10_V) and
       (part not in list_doctor) and
       (part not in list_drug) and
       (part not in list_case)):
        idx += 1
        print(idx)
        list_control.append(str(part))
        
print(len(list_control))
control_numpy = np.array(list_control)
np.savetxt('control_id_gad5.txt', control_numpy, fmt='%s')