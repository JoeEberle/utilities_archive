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
    '''
    the set_talking_code function accepts parameters to configure the talking code capabilities
    '''         
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
    '''
    the set_talking_code_gender sets the text to speech engine to a male or female voice 
    '''            
    global talking_voice_male_gender 
    talking_voice_male_gender = set_gender_male_or_female      
    
# Set True for talking code ON or False for no talking code  
def set_talking_code_on_or_off(set_talking_on_or_off):
    global talking_code     
    talking_code = set_talking_on_or_off

# Initalize and instantiate the text to speech engine      
def initialize_text_to_speech():
    '''
    the initialize_text_to_speech  function intializes the text to speech engine and sets the voice and 
    speaking rate
    '''
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
    '''
    the say  function says whatever speech is sent to it. If talking_code is set True it will speak. 
    If printing_while_talking is set True it will print.
    '''    
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
    '''
    the say  function says whatever speech is sent to it. If talking_code is set True it will speak. 
    If printing_while_talking is set True it will print.
    '''        
    global printing_output # The global setting for if output is supposed to be printed to the console 
    global talking_code    # The global setting for if the code is supposed to explain itself in a human voice
    if printing_output: 
        print(dialog) 
    if talking_code:
        say(dialog)     
        
def list_all_xlsx_files(path):
    '''
    the list_all_xlsx_files function will output a list of files os a specific type
    '''          
    extension = 'xlsx'
    os.chdir(path)
    csv_file_count = 0
    for file in glob.glob('*.{}'.format(extension)):
        csv_file_count += 1 
        out('File #{}   is {} '.format(csv_file_count,file))      
        
def explain_the_project():
    '''
    the explain_the_project function will explain the introduction, credits, high level steps, goals, and glosssary of terms for a 
    project. The explain_the_project function will will either print to console or speak depending on settings. 
    The explain_the_project function will only explain the portion of the project set to True. This human generated may be Slow !
    '''          
    project_explanation = "" 
    if reading_introduction:
        project_explanation = project_explanation + get_introduction()
    if reading_credits:    
        project_explanation = project_explanation + get_credits() 
    if reading_steps:
        project_explanation = project_explanation + get_process_steps()
    if reading_goals:
        project_explanation = project_explanation + get_solution_goals()        
    if reading_terms:
        project_explanation = project_explanation + get_terms()
    return project_explanation        

# The function explain_the_whole_project explains every part of the project : introduction, credits, steps, goals, and glossary of Terms
# Warning!!!! - Because this is human generated voice it is SLOWWWWWW !!!!!!
def explain_the_whole_project():
    '''
    the explain_the_whole_project function will explain the introduction, credits, hegh level steps, goals, and glosssary of terms for a 
    project. The explain_the_project function will will either print to console or speak depending on settings. 
    The explain_the_whole_project function will only explain the whole project regardless of settings. 
    Warning!!!! - Because this is human generated voice it is SLOWWWWWW !!!!!!
    '''        
    project_explanation = "" 
    project_explanation = project_explanation + get_introduction()
    project_explanation = project_explanation + get_credits() 
    project_explanation = project_explanation + get_process_steps()
    project_explanation = project_explanation + get_solution_goals()        
    project_explanation = project_explanation + get_terms()
    return project_explanation   
      
# The function document_the_whole_project prints out the : introduction, credits, steps, goals, and glossary of Terms
def output_the_whole_project():
    '''
    the output_the_whole_project function will output the introduction, credits, hegh level steps, goals, and glosssary of terms for a 
    project to the console
    '''          
    get_introduction()
    get_credits() 
    get_process_steps()
    get_solution_goals()        
    get_terms()  
    get_solution_notes()

def document_the_whole_project():
    '''
    the document_the_whole_project function will output the introduction, credits, hegh level steps, goals, and glosssary of terms for a 
    project to the console
    '''  
    project_documentation = 'This project documentation: \n'
    project_documentation = project_documentation + get_introduction()
    project_documentation = project_documentation + get_credits() 
    project_documentation = project_documentation + get_process_steps()
    project_documentation = project_documentation + get_solution_goals()        
    project_documentation = project_documentation + get_terms()  
    project_documentation = project_documentation + get_solution_notes()
    return project_documentation  

# Introduction - Overview of CSV to SQL Import Process Steps 
def get_credits(): 
    dialog = 'This Jupiter notebook was developed:\n'
    dialog = dialog + 'In collaboration by Joe Eberle and others.\n' 
    dialog = dialog + 'The solution was developed in Python starting on 9/20/2022 and revised on 10/20/2022\n'
    dialog = dialog + 'This solution is free and open source and the code is openly available for general use.\n'    
    return dialog
    
# Introduction - Overview of CSV to SQL Import Process Steps 
def get_terms(): 
    dialog = 'The glossary of terms for this process is :\n'
    dialog = dialog + 'PYTHON. Python is a general-purpose programming language that is widely used for data science.\n'
    dialog = dialog + 'SQL. Structured Query Language (SQL) is commonly used for manipulating and querying data.\n'
    dialog = dialog + 'CSV. A Comma-Separated Values  file (CSV) is a text file in which information is separated by commas.\n'
    dialog = dialog + 'PANDAS. Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.\n'
    dialog = dialog + 'OS PACKAGE - The OS python library provides a portable way of using operating system dependent functionality to allow your python code to run on all platforms.\n'
    dialog = dialog + 'pyttsx3. pyttsx3 is a text-to-speech conversion library in Python that works offline.\n'  
    return dialog    
    
# Process Steps - Overview of CSV to SQL Import Process Steps 
def get_process_steps():
    dialog = 'The high level steps for this solution are:\n'
    dialog = dialog + 'Step 1: Establish the configuration parser engine.\n'
    dialog = dialog + 'Step 2: Establish all the Sections for initial configuration settingsn'
    dialog = dialog + 'Step 3: Write out name value pairs for all of the configuration settings.\n' 
    dialog = dialog + 'Step 4: Repeat steps 2 and 3 until all of the sections and configuration settings are complete.\n'  
    dialog = dialog + 'Step 5: Write out the config.ini file .\n'   
    dialog = dialog + 'Step 6: Test a singular Config.ini setting.\n'   
    dialog = dialog + 'Step 7: Print out the entire config.ini file and visually inspect it.\n'       
    say(dialog) 
    return dialog    
    
# Introduction - Overview of NoteBooks  
def get_introduction():
    dialog = 'This jupiter notebook will establish a configuration file that contains configuration settings.\n'
    dialog = dialog +  'The configuration file will allow you to quickly and easily customize settings and global variables.\n'
    dialog = dialog +  'The configuration file will be maliable allowing users to reset configurations as needed.\n '    
    say(dialog)  
    return dialog    

# Python Design Goals 
def get_solution_goals():
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
    return dialog    
    
# Python Design Goals 
def get_solution_notes():
    dialog = 'The additional notes for this solution are:\n'
    dialog = dialog + 'OCCAMS RAZOR:  OCCAMS razor states that the simplest explanation is preferable to more complex.\n'
    dialog = dialog + 'OCCAMS razor also implies simple theories are easier to verify.\n'
    dialog = dialog + 'NON PYTHONIC: Note that the lower case underscore separated naming convention is a personal preference.\n'    
    say(dialog)    
    return dialog    


def save_documentation(filename):
    '''
            the save_documentation function will save the introduction, credits, hegh level steps, goals, and glosssary of terms in a file               for documentation purposes
    '''  
    documentation = document_the_whole_project()      # get all of the documentation 
    f = open(filename, "a")
    f.write(documentation)
    f.close()
    
    
def read_documentation(filename):
    '''
            the read_documentation function will read in the saved introduction, credits, hegh level steps, goals, and glosssary of terms 
    '''  
    f = open(filename, "r")
    documentation = f.read() 
    return documentation
    

          
    
 