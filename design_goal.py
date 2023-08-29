''' The design_goal_list module manages a list of content.''' 
from dataclasses import dataclass, astuple, asdict

@dataclass
class design_goal_list(object):   
    ''' The design_goal_list class manages a list of content.'''     
                                
    def __init__(self):
        ''' The design_goal_list class __init__ function initializes a set of content.'''            
        import pandas as pd 
        self.df_list = pd.DataFrame()
        self.df_list = self.get_data
        self.introduction = 'The design goals are:'
        self.header = 'Design Goals'    
        self.file_location_excel = 'C:\working_directory\infrastructure_setup\design_goal.xlsx'
        self.html_file_name = 'solution_design_goals.html'     
        self.html = ''             
        
#         self.document = self.output() 

    def get_list_intro(self):  
        ''' The get_list_intro function returns content introduction.'''           
        return(self.introduction) 
    
    def get_header(self):  
        ''' The get_header function returns the content header.'''            
        return(self.header)     
    
    def output(self):  
        ''' The output function returns output formated content.'''         
        self.document = self.get_list_intro() + '\n' 
        for index, row in self.df_list.iterrows():
             self.document = self.document + f'\n{self.df_list.design_goal[index]} {self.df_list.design_goal_description[index]}' 
        return self.document  
    
    def get_html(self):    
        ''' The get_html function returns html formated content.''' 
        self.html =  ''
        self.html =  self.html + '\n<h1>'  + self.get_header() + '</h1>\n'
        self.html =  self.html + '\n<h2>' + self.get_list_intro()  + '</h2>\n' 
        for idx, row in self.df_list.iterrows():
            self.html = self.html + f'\n<li><b>{self.df_list.design_goal[idx]}</b>{self.df_list.design_goal_description[idx]}</li>'
        self.html =  '<html>' + self.html + '\n</html>'          
        return self.html
   
    def get_data(self):
        ''' The get_data function returns in the form of a dataframe.'''         
        import pandas as pd 
        self.df_list = pd.read_excel(self.file_location_excel)
        return self.df_list 
    
    def save_to_excel(self, excel_file_name):
        ''' The save_to_excel function writes the contents to a specified filename.
        :param number_1: this is the full path filename to save the excel into '''            
        if len(excel_file_name) > 2: 
            self.file_location_excel = output_html_file_name
        import pandas as pd 
        self.df_list.to_excel(self.file_location_excel)
        return self.df_list 
      
    def write_html_file(self, output_html_file_name):
        ''' The write_html_file function writes the contents to a specified filename.
        :param output_html_file_name: this is the full path filename to save the html into '''           
        self.html_file_name = 'solution_design_goals.html'   # the default HTML file name to write too 
        if len(output_html_file_name) > 2: 
            self.html_file_name = output_html_file_name
        with open(self.html_file_name, 'w') as html_file:
            html_file.write(self.get_html())
                  
    def write_document_file(self, output_document_file_name):
        ''' The write_document_file function writes the contents to a specified filename.
        :param output_document_file_name: this is the full path filename to save the document into '''           
        document_file_name = 'solution_design_goals_document.doc'   # the default document_file_name file name to write too 
        if len(output_document_file_name) > 2: 
            file_name = output_document_file_name
        with open(file_name, 'w') as document_file:
            document_file.write(self.output())   