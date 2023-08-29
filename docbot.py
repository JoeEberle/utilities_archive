import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import pandas as pd
from datetime import date 
Demo = True

engine = pyttsx3.init()
voices = engine.getProperty('voices')
Doctor_Name = 'Dr Bot'

Excel_fname = '/Health_Bot_Chat_Log.xlsx'
Path_to_Excel = 'c:/Users/josep/Documents/AIHS/'
Chat_log_df = pd.read_excel(Path_to_Excel+Excel_fname)

Prediabetes = 'Prediabetes is a component of the metabolic syndrome and is characterized by elevated blood sugar levels that fall below the threshold to diagnose diabetes mellitus. It usually does not cause symptoms but people with prediabetes often have obesity (especially abdominal or visceral obesity), dyslipidemia with high triglycerides and/or low HDL cholesterol, and hypertension.[1] It is also associated with increased risk for cardiovascular disease (CVD). Prediabetes is more accurately considered an early stage of diabetes as health complications associated with type 2 diabetes often occur before the diagnosis of diabetes.'


def log_chat(Date, User, Question, Response, Intent, Dialogue, Response_Confidence, Chat_Counter):
    Chat_log_df.loc[len(Chat_log_df.index)] = [date.today(), 'jospeheberle@outlook.com', 'Question', 'Response', 'Intent', 'Dialogue', 18, 1]
    return 


def get_chat_Log(log_file_name, path ): 
    Excel_fname = '/Health_Bot_Chat_Log.xlsx'
    Path_to_Excel = 'c:/Users/josep/Documents/AIHS/'
    Chat_log_df = pd.read_csv(Path_to_Excel+Excel_fname)
    return Chat_Log_df

def set_voice(gender):
    ''' Set the voice male or female ''' 
    voices = engine.getProperty('voices')
    if gender == 'male':
        engine.setProperty('voice',voices[0].id)  # Male Voice
    else:    
        engine.setProperty('voice',voices[1].id)  # Female Voice
        
        
def set_voice_id(voice_id):
    ''' Set the voice id for the desired voice ''' 
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[voice_id].id)   
  
        
def set_voice_speed(rate=120):
    ''' Set the voice male or female '''     
    engine.setProperty("rate", rate)  
    
# Saves to a different path leaving the original in place
def learn_patient_data(Excel_fname = 'GPPC_PCP_Lancaster_Transit.xlsx'):
    ''' Set the voice male or female '''     
    import pandas as pd
    Excel_fname = 'GPPC_PCP_Lancaster_Transit.xlsx'
    Path_to_Excel = 'c:/Users/josep/Documents/Kaleida/Attribution_formated/'
    df_attribution = pd.read_excel(Path_to_Excel + Excel_fname)
    df_attribution['Birth  Date'] = df_attribution['Birth  Date'].dt.date     # Transform the Birth_Date from DateTime to Date 
    return df_attribution    

def get_patient_demographic(patient_ID): 
    ''' The get_patient_demographic function returns demographic information on  specific patient ''' 
    Patient_Row = patient_ID 
    Patient_Name = pd_attribution.loc[Patient_Row,'Patient  Name']
    if Demo: 
        Patient_Name = 'Joe Eberle'
        Patient_Name = 'Patient Anonymous'
            
    Patient_Birth_Date = pd_attribution.loc[Patient_Row,'Birth  Date'] 
    Patient_Age = pd_attribution.loc[Patient_Row,'Age']
    Patient_Gender = pd_attribution.loc[Patient_Row,'Gender']
    Patient_Deceased = pd_attribution.loc[Patient_Row,'Deceased']  
    Patient_Deceased_Date = pd_attribution.loc[Patient_Row,'Deceased  Date'] 
    if Patient_Deceased == 1.0:
        Patient_Deceased_Status = f'The patient is identified as deceased as of {Patient_Deceased_Date}'
    else: 
        Patient_Deceased_Status = ''
    Patient_Demographic = f'{Patient_Name} is a {Patient_Age} old {Patient_Gender} born on {Patient_Birth_Date}. {Patient_Deceased_Status}'
    return Patient_Demographic

def get_patient_intro(patient_ID): 
    ''' The get_patient_intro function returns an introduction of a specific patient '''     
    Patient_Row = patient_ID 
    Patient_Name = pd_attribution.loc[Patient_Row,'Patient  Name']
    if Demo: 
        Patient_Name = 'Joe Eberle'
        Patient_Name = 'Patient Anonymous'
    return f'Patient is named: {Patient_Name}'

def get_patient_attribution(patient_ID): 
    Patient_Row = patient_ID 
    Patient_Name = pd_attribution.loc[Patient_Row,'Patient  Name']
    if Demo: 
        Patient_Name = 'Joe Eberle'
        Patient_Name = 'Patient Anonymous'  
    Provider_Name = pd_attribution.loc[Patient_Row,'Provider  Name']
    Organization_Name = pd_attribution.loc[Patient_Row,'Organization  Name']
    Organization_Class = pd_attribution.loc[Patient_Row,'Organization  Class']    
    Patient_Attribution = f'{Patient_Name} is attributed to provider {Provider_Name} who works mainly at {Organization_Name} practice. '
    Patient_Attribution = Patient_Attribution + f'The practice {Organization_Name} is part of the {Organization_Class} network. '
    return Patient_Attribution 

def get_patient_coverage(patient_ID): 
    Patient_Row = patient_ID 
    Patient_Name = pd_attribution.loc[Patient_Row,'Patient  Name']
    if Demo: 
        Patient_Name = 'Joe Eberle'
        Patient_Name = 'Patient Anonymous'
    Payer_Name = pd_attribution.loc[Patient_Row,'Payer  Name']
    Plan_Name = pd_attribution.loc[Patient_Row,'Plan  Name']
    Patient_Coverage = f'{Patient_Name} is covered by {Payer_Name} and is in plan {Plan_Name}. '
    return Patient_Coverage

def get_patient_information(patient_ID): 
    demo = get_patient_demographic(patient_ID)
    attrib = get_patient_attribution(patient_ID)
    coverage = get_patient_coverage(patient_ID)
    Patient_Information = demo + attrib + coverage
    return Patient_Information    

Prediabetes = 'Prediabetes is a component of the metabolic syndrome and is characterized by elevated blood sugar levels that fall below the threshold to diagnose diabetes mellitus. It usually does not cause symptoms but people with prediabetes often have obesity (especially abdominal or visceral obesity), dyslipidemia with high triglycerides and/or low HDL cholesterol, and hypertension.[1] It is also associated with increased risk for cardiovascular disease (CVD). Prediabetes is more accurately considered an early stage of diabetes as health complications associated with type 2 diabetes often occur before the diagnosis of diabetes.'

pd_attribution = learn_patient_data('GPPC_PCP_Lancaster_Transit.xlsx')
 
 