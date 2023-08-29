#!/usr/bin/env python
# coding: utf-8
# In[3]:

__author__      = "Joe Eberle"
__copyright__   = " "

def get_solution_documentation():
    ''' the get_solution_documentation function will return the solution documentation. '''  
    solution_documentation = 'This solution documentation: \n'
    solution_documentation = solution_documentation + get_solution_introduction()
    solution_documentation = solution_documentation + get_credits() 
    solution_documentation = solution_documentation + get_solution_steps()
    solution_documentation = solution_documentation + get_solution_notes()
#     solution_documentation = solution_documentation + get_magic_or_dunder()    
    return solution_documentation  

def save_documentation(filename):
    ''' the save_documentation function will save the solution documentation in a file.'''  
    documentation = get_solution_documentation()      # get all of the documentation 
    f = open(filename, "w")
    f.write(documentation)
    f.close()
     
def get_magic_or_dunder(object):
    ''' the get_magic_or_dunder function will return all of the python magic functions for the class. '''      
    magic_or_dunder = '\n'  # Start with a new line to separate documentation and make it more readable.   
    magic_or_dunder = magic_or_dunder + 'Magic or Dunder:\n'  
    magic_or_dunder = magic_or_dunder + '\n \n __builtins__:' + object.__builtins__ 
    magic_or_dunder = magic_or_dunder + '\n \n __cached__:' + object.__cached__ 
    magic_or_dunder = magic_or_dunder + '\n \n __doc__:' + object.__doc__ 
    magic_or_dunder = magic_or_dunder + '\n \n __file__:' + object.__file__ 
    magic_or_dunder = magic_or_dunder + '\n \n __loader__:' + object.__loader__ 
    magic_or_dunder = magic_or_dunder + '\n \n __name__:' + object.__name__ 
    magic_or_dunder = magic_or_dunder + '\n \n __package__:' + object.__package__ 
    magic_or_dunder = magic_or_dunder + '\n \n __spec__:' + object.__spec__ 
    magic_or_dunder = magic_or_dunder + '\n \n __spec__:' + object.__author__     
    return magic_or_dunder

# get_credits - returns who contributed to the solution and when.
def get_credits(): 
    ''' the get_credits function will return who contributed to the solution and when. '''         
    solution_credits = '\n'   # Start with a new line to separate documentation and make it more readable.   
    solution_credits = solution_credits + 'This Jupiter notebook was developed:\n'
    solution_credits = solution_credits + 'In collaboration by Joe Eberle and others.\n' 
    solution_credits = solution_credits + 'The solution was developed in Python starting on 11/03/2022 and revised on 11/03/2022\n'
    solution_credits = solution_credits + 'This solution is free and open source and the code is openly available for general use.\n\n'   
    return solution_credits 
    
# get_solution_steps- Overview of solution Process Steps 
def get_solution_steps():
    ''' the get_solution_steps function will return high levels steps needed for the solution. '''        
    solution_steps = '\n'   # Start with a new line to separate documentation and make it more readable.     
    solution_steps = 'The high level steps for this solution are:\n'
    solution_steps = solution_steps + 'Step 1: pip install all librairies used.\n'
    solution_steps = solution_steps + 'Step 2: test all STANDARD libraries by importing them and visually inspecting for import errors. \n'
    solution_steps = solution_steps + 'Step 3:test all NON STANDARD or custom libraries by importing them and visually inspecting for import errors. \n\n' 
    return solution_steps 
    
# Introduction - Overview of Solution  
def get_solution_introduction():
    ''' the get_solution_introduction function returns the and overview or introduction of what the solution does. '''  
    solution_introduction = '\n'   # Start with a new line to separate documentation and make it more readable.     
    solution_introduction = solution_introduction + 'This jupiter notebook will install and update all libraries.\n'
    solution_introduction = solution_introduction + 'This solution is easily extended to include any libraries you choose.\n'    
    return solution_introduction 
   
#  get_solution_notes
def get_solution_notes():
    ''' the get_solution_notes function returns any special or helpful notes about the solution.'''  
    solution_notes = '\n \n'   # Start with a new line to separate documentation and make it more readable. 
    solution_notes = solution_notes + 'The additional notes for this solution are: \n'
    solution_notes = solution_notes + 'Note 1: This solution assumes that the entire development team is OK using the latest libraries and technologies. This may not be true and is personal preference. Some solutions may fail using this approach if the latest libraries are not backwardly compatiable or methods are replaced or redacted. Some organizations or indviduals may prefer to use virtual environments to avoid these types of issues. This is personal preference and an architecture decision for you to consider when choosing whats best for you or your organization.\n'  
    solution_notes = solution_notes + 'Note 2: This solution assumes that PIP is intelligent enough to determine if libraries are installed or outdated. PIP is the package installer for Python. PIP is the de facto and recommended package-management system written in Python and is used to install and manage software packages. It connects to an online repository of public packages, called the Python Package Index.\n' 
    solution_notes = solution_notes + 'Note 3: A monolithic (brute force) library update approach was chosen as the default approach for this solution meaning that a comprehensive set of libraries is used for ALL solutions, however, there is nothing preventing you from createing and using individual library installer for each solution you develop. This is personal preference and an architecture decision for you to consider when choosing whats best for you or your organization. \n'    
    solution_notes = solution_notes + 'Note 4: This data science solution was developed in python using jupyter notebook for ease of illustration an educational purposes. Their is nothing preventing you from using your preferred language and integrated development environment (IDE) of your choice such as visual studio or pycharm. This solution was devloped on a windows platform and has not been tested on linux or othewr operating systems however and it was designed with cross-platform compatible libraries so hypothetically the solution should be portable to other platforms. \n'  
    solution_notes = solution_notes + 'Note 5: The performance of this solution will vary greatly based upon how often it is run and how many libraries need installation or updating. \n'   
    solution_notes = solution_notes + 'Note 6: The solution also includes a section that tests custom (private) or non standards PiPY publically compatible libraries. This section of the solution may be removed if it is not applicable to your solutions. \n'     
    return solution_notes 


