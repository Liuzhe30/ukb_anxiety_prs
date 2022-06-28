import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
import warnings

warnings.filterwarnings('ignore')

# full table
data = pd.read_csv('covariables/2_is_anxiety.csv')
first_rows = data.head(5)
print(first_rows)
print(len(data))

columns = ['FID','IID','Is_anxiety','Age', 'Sex', 'BMI', 'Smoking', 'TDI', 'Alcohol_drinking', 'Ethnic',
           'Diabetes', 'Cancer', 'COPD', 'Health_score', 'Income_score', 'Qualifications', 'Cooked_vegetable_intake', 
           'Salad/raw_vegetable_intake', 'Fresh_fruit_intake', 'Dried_fruit_intake', 'Oily_fish_intake', 'Poultry_intake',
           'Beef_intake', 'Lamb/mutton_intake', 'Pork_intake', 'Cheese_intake', 'Milk_type_used', 'Cereal_type', 'Bread_type', 'Salt_added_to_food',
           'Tea_intake', 'Coffee_type', 'Water_intake', 'Coffee_intake', 'Processed_meat_intake', 'Non_oily_fish_intake', 
           'Genetic_PCA1', 'Genetic_PCA2', 'Genetic_PCA3', 'Genetic_PCA4', 'Genetic_PCA5', 'Genetic_PCA6',
           'Genetic_PCA7', 'Genetic_PCA8', 'Genetic_PCA9', 'Genetic_PCA10', 'Cluster_CR', 'dQC', 'Cardiovascular_disease', 'Gastrointestinal/abdominal']

# card list
card_list = []
card_csv = pd.read_csv('covariables/cov-card_participant.csv')
for i in range(len(card_csv)):
    FID = str(card_csv['eid'][i])
    card_list.append(FID)

# card list
gastr_list = []
gastr_csv = pd.read_csv('covariables/cov-gastr_participant.csv')
for i in range(len(gastr_csv)):
    FID = str(gastr_csv['eid'][i])
    gastr_list.append(FID)

data_new = pd.DataFrame()
for i in range(len(data)):
    FID = str(data['FID'][i])
    row_data = data.iloc[[i]]
    # Not answer/ don't know -NA
    row_data.replace('Prefer not to answer', 'NA', inplace = True)
    row_data.replace('Do not know', 'NA', inplace = True)
    row_data.fillna('missing', inplace = True)
    
    # Sex, Female-1, Male-0
    if(row_data['Sex'][i] == 'Female'):
        row_data['Sex'][i] = 1
        row_data['Sex'] = row_data['Sex'].astype(int)
    elif(row_data['Sex'][i] == 'Male'):
        row_data['Sex'][i] = 0
        row_data['Sex'] = row_data['Sex'].astype(int)
    
    # Smoking, Current-2, Previous-1, Never-0
    if(row_data['Smoking'][i] == 'Current'):
        row_data['Smoking'][i] = 2
        row_data['Smoking'] = row_data['Smoking'].astype(int)
    elif(row_data['Smoking'][i] == 'Previous'):
        row_data['Smoking'][i] = 1
        row_data['Smoking'] = row_data['Smoking'].astype(int)
    elif(row_data['Smoking'][i] == 'Never'):
        row_data['Smoking'][i] = 0 
        row_data['Smoking'] = row_data['Smoking'].astype(int)     
    
    # Alcohol_drinking, Current-2, Previous-1, Never-0
    if(row_data['Alcohol_drinking'][i] == 'Current'):
        row_data['Alcohol_drinking'][i] = 2
        row_data['Alcohol_drinking'] = row_data['Alcohol_drinking'].astype(int)
    elif(row_data['Alcohol_drinking'][i] == 'Alcohol_drinking'):
        row_data['Alcohol_drinking'][i] = 1
        row_data['Alcohol_drinking'] = row_data['Alcohol_drinking'].astype(int)
    elif(row_data['Alcohol_drinking'][i] == 'Never'):
        row_data['Alcohol_drinking'][i] = 0 
        row_data['Alcohol_drinking'] = row_data['Alcohol_drinking'].astype(int)   
    
    # Ethnic
    if(row_data['Ethnic'][i] in ['British', 'Irish', 'Any other white background']):
        row_data['Ethnic'][i] = 1
        row_data['Ethnic'] = row_data['Ethnic'].astype(int)  
    elif(row_data['Ethnic'][i] != 'missing'):
        row_data['Ethnic'][i] = 0
        row_data['Ethnic'] = row_data['Ethnic'].astype(int)        
    
    # Diabetes
    if(row_data['Diabetes'][i][0:3] == 'Yes'):
        row_data['Diabetes'][i] = 1   
        row_data['Diabetes'] = row_data['Diabetes'].astype(int)
    elif(row_data['Diabetes'][i] == 'No'):
        row_data['Diabetes'][i] = 0 
        row_data['Diabetes'] = row_data['Diabetes'].astype(int)
    
    # Cancer
    if(row_data['Cancer'][i][0:3] == 'Yes'):
        row_data['Cancer'][i] = 1   
        row_data['Cancer'] = row_data['Cancer'].astype(int)
    elif(row_data['Cancer'][i] == 'No'):
        row_data['Cancer'][i] = 0 
        row_data['Cancer'] = row_data['Cancer'].astype(int)    
    
    # COPD
    row_data['COPD'] = row_data['COPD'].astype(str)  
    if(row_data['COPD'][i][0:3] == 'Yes'):
        row_data['COPD'][i] = 1   
        row_data['COPD'] = row_data['COPD'].astype(int)
    elif(row_data['COPD'][i] == 'No'):
        row_data['COPD'][i] = 0 
        row_data['COPD'] = row_data['COPD'].astype(int)    
    
    # Qualifications
    if(row_data['Qualifications'][i].split()[0] == 'College'):
        row_data['Qualifications'][i] = 5   
        row_data['Qualifications'] = row_data['Qualifications'].astype(int)
    elif(row_data['Qualifications'][i].split()[0] == 'A'):
        row_data['Qualifications'][i] = 4 
        row_data['Qualifications'] = row_data['Qualifications'].astype(int)
    elif(row_data['Qualifications'][i].split()[0] == 'O'):
        row_data['Qualifications'][i] = 3 
        row_data['Qualifications'] = row_data['Qualifications'].astype(int)        
    elif(row_data['Qualifications'][i].split()[0] == 'CSEs'):
        row_data['Qualifications'][i] = 2 
        row_data['Qualifications'] = row_data['Qualifications'].astype(int)
    elif(row_data['Qualifications'][i].split()[0] == 'NVQ'):
        row_data['Qualifications'][i] = 1 
        row_data['Qualifications'] = row_data['Qualifications'].astype(int) 
    elif(row_data['Qualifications'][i].split()[0] in ['Other', 'None']):
        row_data['Qualifications'][i] = 0 
        row_data['Qualifications'] = row_data['Qualifications'].astype(int)        
    
    ############ Diet ################
    # type1 : Cooked_vegetable_intake Salad/raw_vegetable_intake Fresh_fruit_intake Dried_fruit_intake Tea_intake Water_intake Coffee_intake
    # less than one: 0
    
    type1_list = ['Cooked_vegetable_intake', 'Salad/raw_vegetable_intake', 'Fresh_fruit_intake', 'Dried_fruit_intake', 'Tea_intake', 'Water_intake', 'Coffee_intake']
    for type1 in type1_list:
        if(row_data[type1][i] == 'Less than one'):
            row_data[type1][i] = 0
            row_data[type1] = row_data[type1].astype(int)        
    
    # type2 : Oily_fish_intake Poultry_intake Beef_intake Lamb/mutton_intake Pork_intake Cheese_intake Processed_meat_intake Non_oily_fish_intake
    # Never/Less than once-0, Once-1, 2~4-2, 5~6-3, daily-4
    type2_list = ['Oily_fish_intake', 'Poultry_intake', 'Beef_intake', 'Lamb/mutton_intake', 'Pork_intake', 'Cheese_intake', 'Processed_meat_intake', 'Non_oily_fish_intake']
    for type2 in type2_list:
        if(row_data[type2][i] in ['Less than once a week', 'Never']):
            row_data[type2][i] = 0
            row_data[type2] = row_data[type2].astype(int)
        elif(row_data[type2][i] == 'Once a week'):
            row_data[type2][i] = 1
            row_data[type2] = row_data[type2].astype(int)
        elif(row_data[type2][i].split()[0] == '2-4'):
            row_data[type2][i] = 2
            row_data[type2] = row_data[type2].astype(int)  
        elif(row_data[type2][i].split()[0] == '5-6'):
            row_data[type2][i] = 3
            row_data[type2] = row_data[type2].astype(int)
        elif(row_data[type2][i] == 'Once or more daily'):
            row_data[type2][i] = 4
            row_data[type2] = row_data[type2].astype(int)     
            
    # type3 : Milk_type_used Cereal_type Bread_type Salt_added_to_food  
    if(row_data['Milk_type_used'][i].split()[0] == 'Full'):
        row_data['Milk_type_used'][i] = 4
        row_data['Milk_type_used'] = row_data['Milk_type_used'].astype(int) 
    elif(row_data['Milk_type_used'][i].split('-')[0] == 'Semi'):
        row_data['Milk_type_used'][i] = 3
        row_data['Milk_type_used'] = row_data['Milk_type_used'].astype(int) 
    elif(row_data['Milk_type_used'][i] == 'Skimmed'):
        row_data['Milk_type_used'][i] = 2
        row_data['Milk_type_used'] = row_data['Milk_type_used'].astype(int) 
    elif(row_data['Milk_type_used'][i] == 'Soya'):
        row_data['Milk_type_used'][i] = 1
        row_data['Milk_type_used'] = row_data['Milk_type_used'].astype(int)
    elif(row_data['Milk_type_used'][i].split()[0] == 'Other'):
        row_data['Milk_type_used'][i] = 0
        row_data['Milk_type_used'] = row_data['Milk_type_used'].astype(int)
    elif(row_data['Milk_type_used'][i].split('/')[0] == 'Never'):
        row_data['Milk_type_used'][i] = 'missing' 
        
    if(row_data['Cereal_type'][i].split()[0] == 'Bran'):
        row_data['Cereal_type'][i] = 4
        row_data['Cereal_type'] = row_data['Cereal_type'].astype(int)
    elif(row_data['Cereal_type'][i].split()[0] == 'Biscuit'):
        row_data['Cereal_type'][i] = 3
        row_data['Cereal_type'] = row_data['Cereal_type'].astype(int)
    elif(row_data['Cereal_type'][i].split()[0] == 'Oat'):
        row_data['Cereal_type'][i] = 2
        row_data['Cereal_type'] = row_data['Cereal_type'].astype(int)
    elif(row_data['Cereal_type'][i].split()[0] == 'Muesli'):
        row_data['Cereal_type'][i] = 1
        row_data['Cereal_type'] = row_data['Cereal_type'].astype(int)
    elif(row_data['Cereal_type'][i].split()[0] == 'Other'):
        row_data['Cereal_type'][i] = 0
        row_data['Cereal_type'] = row_data['Cereal_type'].astype(int)  
        
    if(row_data['Bread_type'][i].split()[0] == 'White'):
        row_data['Bread_type'][i] = 3
        row_data['Bread_type'] = row_data['Bread_type'].astype(int)
    elif(row_data['Bread_type'][i].split()[0] == 'Brown'):
        row_data['Bread_type'][i] = 2
        row_data['Bread_type'] = row_data['Bread_type'].astype(int)
    elif(row_data['Bread_type'][i].split()[0] == 'Wholemeal'):
        row_data['Bread_type'][i] = 1
        row_data['Bread_type'] = row_data['Bread_type'].astype(int) 
    elif(row_data['Bread_type'][i].split()[0] == 'Other'):
        row_data['Bread_type'][i] = 0
        row_data['Bread_type'] = row_data['Bread_type'].astype(int)   
        
    if(row_data['Salt_added_to_food'][i] == 'Always'):
        row_data['Salt_added_to_food'][i] = 3
        row_data['Salt_added_to_food'] = row_data['Salt_added_to_food'].astype(int)
    elif(row_data['Salt_added_to_food'][i] == 'Usually'):
        row_data['Salt_added_to_food'][i] = 2
        row_data['Salt_added_to_food'] = row_data['Salt_added_to_food'].astype(int)
    elif(row_data['Salt_added_to_food'][i] == 'Sometimes'):
        row_data['Salt_added_to_food'][i] = 1
        row_data['Salt_added_to_food'] = row_data['Salt_added_to_food'].astype(int)
    elif(row_data['Salt_added_to_food'][i] == 'Never/rarely'):
        row_data['Salt_added_to_food'][i] = 0
        row_data['Salt_added_to_food'] = row_data['Salt_added_to_food'].astype(int)           
        
    if(row_data['Coffee_type'][i].split()[0] == 'Decaffeinated'):
        row_data['Coffee_type'][i] = 3
        row_data['Coffee_typed'] = row_data['Coffee_type'].astype(int)
    elif(row_data['Coffee_type'][i].split()[0] == 'Instant'):
        row_data['Coffee_type'][i] = 2
        row_data['Coffee_typed'] = row_data['Coffee_type'].astype(int)
    elif(row_data['Coffee_type'][i].split()[0] == 'Ground'):
        row_data['Coffee_type'][i] = 1
        row_data['Coffee_typed'] = row_data['Coffee_type'].astype(int) 
    elif(row_data['Coffee_type'][i].split()[0] == 'Other'):
        row_data['Coffee_type'][i] = 0
        row_data['Coffee_typed'] = row_data['Coffee_type'].astype(int)     
    
    ######## Cardiovascular_disease and Gastrointestinal/abdominal ########
    # Cardiovascular_disease
    if(FID in card_list):
        row_data['Cardiovascular_disease'] = 1
        row_data['Cardiovascular_disease'] = row_data['Cardiovascular_disease'].astype(int)
    else:
        row_data['Cardiovascular_disease'] = 0
        row_data['Cardiovascular_disease'] = row_data['Cardiovascular_disease'].astype(int)   
        
    # Gastrointestinal/abdominal
    if(FID in gastr_list):
        row_data['Gastrointestinal/abdominal'] = 1
        row_data['Gastrointestinal/abdominal'] = row_data['Gastrointestinal/abdominal'].astype(int)
    else:
        row_data['Gastrointestinal/abdominal'] = 0
        row_data['Gastrointestinal/abdominal'] = row_data['Gastrointestinal/abdominal'].astype(int)        
    
    
    data_new = pd.concat([data_new, row_data], axis = 0)
    data_new.replace('missing', 'NA', inplace = True)
    #print(data_new)
    data_new.to_csv('covariables/3_final_numclass.csv', index=None, columns=columns)
    
    
data_new = data_new.reset_index(drop=True)   
print(data_new)     
print(len(data_new))

# save
data_new.to_csv('covariables/3_final_numclass.csv', index=None, columns=columns)
    