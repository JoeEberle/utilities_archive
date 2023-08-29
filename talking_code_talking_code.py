#!/usr/bin/env python
# coding: utf-8
# In[3]:

import pyttsx3

Reading_Intro = True
Reading_Credits = True
Reading_Steps = True 
Reading_Goals = True 
Reading_Terms = True 
Talking_Code = False
Talking_Voice_Male_Gender = True     

def set_talking_code_Settings(Intro_Setting, Credits_Setting, Steps_Setting, Goals_Setting, Terms_Setting, Talking_Code_Setting, Talking_Gender ):
    global Reading_Intro 
    global Reading_Credits 
    global Reading_Steps 
    global Reading_Goals 
    global Reading_Terms 
    global Talking_Code 
    global Talking_Voice_Male_Gender 
    Reading_Intro = Intro_Setting
    Reading_Credits = Credits_Setting  
    Reading_Steps = Steps_Setting
    Reading_Goals = Goals_Setting  
    Reading_Terms = Terms_Setting
    Talking_Code = Talking_Code_Setting
    Talking_Voice_Male_Gender = Talking_Gender 
 
    
def Initialize_Text_to_Speach():
    Text_to_Speech = pyttsx3.init()
    Text_to_Speech.setProperty('Rate',187)
    voices = Text_to_Speech.getProperty('voices')
    if Talking_Voice_Male_Gender:
        Text_to_Speech.setProperty('voice', voices[0].id)    # Default Male voice registered as 'Dave'
    else: 
        Text_to_Speech.setProperty('voice', voices[1].id)    # Alternate Female voice registered as 'Tina'
    speech = 'The text to speech engine is initialized using pythons pyttsx3 engine'
    Text_to_Speech.say(speech)
    Text_to_Speech.runAndWait()
    return Text_to_Speech
    
# Say Whatever the user wants 
def say(speech):
    printing_while_talking = True 
    if printing_while_talking:
        print('\n')
        print(speech)
    Text_to_Speech = pyttsx3.init()
    Text_to_Speech.say(speech)
    Text_to_Speech.runAndWait()         

# Introduction - Overview of CSV to SQL Import Process Steps 
def read_credits(): 
    Dialog = 'This Jupiter Notebook Was:\n'
    Dialog = Dialog + 'Developed in Collaboration by Joe Eberle\n'
    Dialog = Dialog + 'Developed in Python 3 starting on 9/20/2022\n'
    Dialog = Dialog + 'This package is free AND Open Source and the code is openly available for general Use.\n'    
    say(Dialog)         
    
# Introduction - Overview of CSV to SQL Import Process Steps 
def read_terms(): 
    Dialog = 'The terminology for this process is :\n'
    Dialog = Dialog + 'Python. Python is a general-purpose programming language that is widely used for data science.\n'
    Dialog = Dialog + 'pyttsx3 PACKAGE - The pyttsx3 library is a text to speech engine that is customizable to multiple voices and settings.\n'
    say(Dialog)  
    
# Process Steps - Overview of CSV to SQL Import Process Steps 
def read_process_steps():
    Dialog = 'The steps of this process are :\n'
    Dialog = Dialog + 'Optional Install: Pip or conda install the latest pytsx3 library if not already Loaded \n'
    Dialog = Dialog + 'Step 1: Import the pytsx3 text to speech library.\n'
    Dialog = Dialog + 'Step 2: Instantiate the text to speech engine.\n'
    Dialog = Dialog + 'Step 3: Test the Project dialogues to ensure text to speech is working.\n'
    say(Dialog) 

# Introduction - Overview of NoteBooks  
def read_introduction():
    Dialog = 'This jupiter notebook will quickly and easily setup text to speech so '
    Dialog = Dialog +  'that the code can explain itself and reduce learning curve.\n'
    say(Dialog)  

# Python Design Goals 
def read_solution_goals():
    Dialog = 'The design goals for this code are :\n'
    Dialog = Dialog + 'EXTENSIBILITY: Extensibility is a ability to add additional elements and features to its existing solution.\n'
    Dialog = Dialog + 'MAINTAINABILITY: The ability to easily maintain the solution.\n'
    Dialog = Dialog + 'ACCESSIBILITY: The ability to easily access and use the solution from anywhere.\n'
    Dialog = Dialog + 'SECURITY: To secure the solution and data is only available to those who who have appropriate access.\n' 
    Dialog = Dialog + 'RELIABILITY: The code works consistently and can be counted on from a business perspective. \n' 
    Dialog = Dialog + 'CONSISTENCY: Consistency means having code work reliable and in the same manner every time. \n'
    Dialog = Dialog + 'PERFORMANT: The solution performs quickly enough to meet the business demand.\n'
    Dialog = Dialog + 'INTELLIGENT: The solution learns or provides new insights.\n'
    Dialog = Dialog + 'SIMPLE: The solution should be lean and choose the simplist method of achievement.\n'
    Dialog = Dialog + 'Pythonic: If the solution is built in python it is built using the python way. Pythonic code should be best practice. Pythonic code should be highly performant. \n'
    Dialog = Dialog + 'NO CODE - LOW CODE: the solution should be lean, agile, modular, and efficient. The solution should be minimal or no code required.\n'
    say(Dialog)   

   
    
def out(dialog):
    if printing_output: 
        print(dialog) 
    if Talking_Code:
        say(dialog)     
        
def list_all_xlsx_files(path):
    extension = 'xlsx'
    os.chdir(path)
    csv_file_count = 0
    for file in glob.glob('*.{}'.format(extension)):
        csv_file_count += 1 
        out('File #{}   is {} '.format(csv_file_count,file))             
        
def explain_the_project():
    if Reading_Intro:
        read_introduction()
    if Reading_Credits:    
        read_credits() 
    if Reading_Steps:
        read_process_steps()
    if Reading_Goals:
        read_solution_goals()        
    if Reading_Terms:
        read_terms()        
        
        

