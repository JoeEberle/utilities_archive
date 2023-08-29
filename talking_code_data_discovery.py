#!/usr/bin/env python
# coding: utf-8
# In[3]:

import pyttsx3
reading_introduction = True
reading_credits = True
reading_steps = True 
reading_goals = True 
reading_terms = True 
talking_code = False
talking_voice_male_gender = True     
printing_while_talking = True 
printing_output = True 

# The set_talking_code method configures most of the settings for talking code utilizing test to speech  
def set_talking_code(introduction, credits, steps, goals, terms, set_talking_on_or_off, set_gender_male_or_female):
    global reading_introduction 
    global reading_credits 
    global reading_steps 
    global reading_goals 
    global reading_terms 
    global talking_code 
    global talking_voice_male_gender 
    reading_introduction = introduction
    reading_credits = credits  
    reading_steps = steps
    reading_goals = goals  
    Reading_terms = terms
    talking_code = talking_code
    talking_voice_male_gender = set_gender_male_or_female     
    
# Set True for Male or false for female 
def set_talking_code_gender(set_gender_male_or_female):
    global talking_voice_male_gender 
    talking_voice_male_gender = set_gender_male_or_female      
    
# Set True for talking code ON or False for no talking code  
def set_talking_code_on_or_off(set_talking_on_or_off):
    global talking_code     
    talking_code = set_talking_on_or_off

# Initalize and instantiate the text to speech engine      
def initialize_text_to_speech():
    text_to_speech = pyttsx3.init()
    text_to_speech.setProperty('Rate',187)
    voices = text_to_speech.getProperty('voices')
    if talking_voice_male_gender:
        text_to_speech.setProperty('voice', voices[0].id)    # Default Male voice registered as 'Dave'
    else: 
        text_to_speech.setProperty('voice', voices[1].id)    # Alternate Female voice registered as 'Tina'
    speech = 'The text to speech engine is initialized using pythons pyttsx3 engine'
    if talking_code:
        text_to_speech.say(speech)
        text_to_speech.runAndWait()
    return text_to_speech
    
# Say Whatever the user wants 
def say(speech):
    global printing_while_talking # The global setting for if output is supposed to be printed to the console     
    global printing_output # The global setting for if output is supposed to be printed to the console 
    global talking_code    # The global setting for if the code is supposed to explain itself in a human voice    
    printing_while_talking = True 
    if printing_while_talking:
        print('\n')
        print(speech)
    if talking_code:     
        text_to_speech = pyttsx3.init()
        text_to_speech.say(speech)
        text_to_speech.runAndWait()         
    
def out(dialog):
    global printing_output # The global setting for if output is supposed to be printed to the console 
    global talking_code    # The global setting for if the code is supposed to explain itself in a human voice
    if printing_output: 
        print(dialog) 
    if talking_code:
        say(dialog)     
        
def list_all_xlsx_files(path):
    extension = 'xlsx'
    os.chdir(path)
    csv_file_count = 0
    for file in glob.glob('*.{}'.format(extension)):
        csv_file_count += 1 
        out('File #{}   is {} '.format(csv_file_count,file))      
        
def explain_the_project():
    if reading_introduction:
        read_introduction()
    if reading_credits:    
        read_credits() 
    if reading_steps:
        read_process_steps()
    if reading_goals:
        read_solution_goals()        
    if reading_terms:
        read_terms()     

# The function explain_the_whole_project explains every part of the project : introduction, credits, steps, goals, and glossary of Terms
# Warning!!!! - Because this is human generated voice it is SLOWWWWWW !!!!!!
def explain_the_whole_project():
    read_introduction()
    read_credits() 
    read_process_steps()
    read_solution_goals()        
    read_terms() 
      
# The function document_the_whole_project prints out the : introduction, credits, steps, goals, and glossary of Terms
def document_the_whole_project():
    read_introduction()
    read_credits() 
    read_process_steps()
    read_solution_goals()        
    read_terms()  
    read_solution_notes()

# Introduction - Overview of CSV to SQL Import Process Steps 
def read_credits(): 
    dialog = 'This Jupiter notebook was developed:\n'
    dialog = dialog + 'In collaboration by Joe Eberle and others including Alan Calhoun, Helmi (Al) Seoud\n' 
    dialog = dialog + 'The solution was developed in Python starting on 9/20/2022\n'
    dialog = dialog + 'This solution is free and Open Source and the code is openly available for general use.\n '    
    say(dialog)         
    
# Introduction - Overview of CSV to SQL Import Process Steps 
def read_terms(): 
    dialog = 'The glossary of terms for this process is :\n'
    dialog = dialog + 'PYTHON. Python is a general-purpose programming language that is widely used for data science.\n'
    dialog = dialog + 'SQL. Structured Query Language (SQL) is commonly used for manipulating and querying data.\n'
    dialog = dialog + 'CSV. A Comma-Separated Values  file (CSV) is a text file in which information is separated by commas.\n'
    dialog = dialog + 'PANDAS. Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.\n'
    dialog = dialog + 'OS PACKAGE - The OS python library provides a portable way of using operating system dependent functionality to allow your python code to run on all platforms.\n'
    dialog = dialog + 'pyttsx3. pyttsx3 is a text-to-speech conversion library in Python that works offline.\n'  
    say(dialog)  
    
# Process Steps - Overview of CSV to SQL Import Process Steps 
def read_process_steps():
    dialog = 'The data flow for this process is :\n'
    dialog = dialog + 'Step 1: Establish The Root Directory to search for data files under.\n'
    dialog = dialog + 'Step 2: Walk the directory structure discovering data to discover all data directories\n'
    dialog = dialog + 'Step 3: Discover all the CSV files or Excel data and register them for future import.\n'
    dialog = dialog + 'Step 4: Save the registry of files to import.\n' 
    say(dialog) 
    
# Introduction - Overview of NoteBooks  
def read_introduction():
    dialog = 'This jupiter notebook will discover all of the raw data files under a specified directory and register them.\n'
    dialog = dialog +  'The files that are discovered will be placed in a registry for future import.\n '
    say(dialog)  

# Python Design Goals 
def read_solution_goals():
    dialog = 'The design goals for this code are :\n'
    dialog = dialog + 'EXTENSIBILITY: Extensibility is an ability to add or extend additional elements and features to the existing code.\n'
    dialog = dialog + 'MAINTAINABILITY: The ability to easily maintain the solution.\n'
    dialog = dialog + 'ACCESSIBILITY: The ability to easily access and use the solution from anywhere.\n'
    dialog = dialog + 'SECURITY: To secure the solution and data is only available to those who who have appropriate access.\n' 
    dialog = dialog + 'RELIABILITY: The code works consistently and can be counted on from a business perspective.\n' 
    dialog = dialog + 'CONSISTENCY: Consistency means having code work reliably and in the same manner every time.\n'
    dialog = dialog + 'PERFORMANT: The solution performs quickly enough to meet the business demand.\n'
    dialog = dialog + 'INTELLIGENT: The solution learns or provides new insights.\n'
    dialog = dialog + 'SIMPLE: The solution should be lean and choose the simplist method of achievement.\n'
    dialog = dialog + 'SELF DOCUMENTING: The code should be able to produce its own documentation.\n'    
    dialog = dialog + 'TALKING: The code should be smart enough to explain itself to a non technical human.\n'        
    dialog = dialog + 'PYTHONIC: If the solution is built in python it is built using the python way.\n'
    dialog = dialog + 'NO CODE - LOW CODE: The solution should contain the minimal code or no code required to achieve objective.\n '
    say(dialog)   
    
# Python Design Goals 
def read_solution_notes():
    dialog = 'The additional notes for this solution are:\n'
    dialog = dialog + 'OCCAMS RAZOR:  OCCAMS razor states that the simplest explanation is preferable to more complex.\n'
    dialog = dialog + 'OCCAMS razor also implies simple theories are easier to verify.\n'
    dialog = dialog + 'NON PYTHONIC: Note that the lower case underscore separated naming convention is a personal preference.\n'    
    say(dialog)      

def column_create_SQL (import_df):
    column_name_List = [x.title() for x in import_df.columns] # Create a List of Columns 
    column_Str =  (', '.join(column_name_List)) # Convert List into one String with commas 
    out('Columns =',column_Str)  
    return column_Str            
    
 