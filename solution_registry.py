class solution_registry(object):

    def __init__(self, solution_name, solution_description):
        self.solution_name = solution_name
        self.solution_description = solution_description

    def output(self):
        return ' {} {} '.format(self.solution_name, self.solution_description)
    
    def get_item(self):
        return self.solution_name
    
    def get_description(self):
        return self.solution_description        
    
    def output_html(self):
        return ' <li><b> {} </b> {}  </li>'.format(self.solution_name, self.solution_description)    
                                
class solution_registry_list(object):   
                                
    def __init__(self):
        self.solution_registry_list = [] 
        self.compose_solution_registry()
        self.document = self.output() 

    def compose_solution_registry(self):
        self.solution_registry_list.append(solution_registry('library_installer','A easy to use utility that updates or installs libraries')) 
        self.solution_registry_list.append(solution_registry('design_goals','A solution to manage a set of fundamental design objectives for technology solutions'))  
        self.solution_registry_list.append(solution_registry('glossary_terms','A solution to manage a set of technical terms and gloassary.'))  
        self.solution_registry_list.append(solution_registry('solution_registry','A solution to manage a set of technical solutions.')) 
        
        self.solution_registry_list.append(solution_registry('task_scheduler','A lightweight easy to use solution to schedule jobs and tasks.')) 
        self.solution_registry_list.append(solution_registry('data_discovery','A solution to walk a a set of directories and discover file content.'))  
        self.solution_registry_list.append(solution_registry('configuring_settings','This solution manages configuration settings'))  
        self.solution_registry_list.append(solution_registry('organization_quality','A solution that identifies gaps in care and evaluates provider and organizational quality and produces ranked score cards.'))  
        
        self.solution_registry_list.append(solution_registry('organization_wellvisit','A solution that identifies gaps in wellness visits and evaluates provider quality and produces ranked score cards.')) 
        self.solution_registry_list.append(solution_registry('schema_generator','A solution that automatically generates schemas based upon raw file formats'))  
        self.solution_registry_list.append(solution_registry('talk_to_me','A text to speech application that explains technology solutions'))  
        self.solution_registry_list.append(solution_registry('event_log','A logging and debugging tool that tracks and analysis steps in a solutions process'))  
        self.solution_registry_list.append(solution_registry('Doc AI','A AI health bot that can learn and answer questions about any location on the web.')) 
    
    def get_header(self):  
        return('Solution Registry')     
    
    def append_item(self, item_name, item_description):  
        self.solution_registry_list.append(solution_registry(item_name, item_description))    

    def get_list_intro(self):  
        return('The registry of solutions are :') 
    
    def append_item(self, item_name, item_description):  
        self.solution_registry_list.append(solution_registry(item_name, item_description))         
    
    def output(self):  
        newline = '\n'
        self.document = self.get_list_intro() + newline 
        for dg in self.solution_registry_list:
            self.document = self.document + dg.output() + newline 
        return   self.document  
    
    def output_html(self):  
        newline = '\n'
        self.document_html = ''
        self.document_html =  self.document_html + newline + '<h1>'  + self.get_header() + '</h1>' +  newline 
        self.document_html =  self.document_html + newline + '<h2>' + self.get_list_intro()  + '</h2>' + newline  + newline        
        for gt in self.solution_registry_list:
            self.document_html = self.document_html + gt.output_html() + newline 
        self.document_html =  '<html>'  + self.document_html   + newline  + '</html>'          
        return self.document_html
    
    def append_item(self, item_name, item_description):  
        self.solution_registry_list.append(solution_registry(item_name, item_description))         
    
    def output(self):  
        newline = '\n'
        self.document = self.get_list_intro() + newline 
        for dg in self.solution_registry_list:
            self.document = self.document + dg.output() + newline 
        return   self.document  
    
    def output_html(self):  
        newline = '\n'
        self.document_html = ''
        self.document_html =  self.document_html + newline + '<h1>'  + self.get_header() + '</h1>' +  newline 
        self.document_html =  self.document_html + newline + '<h2>' + self.get_list_intro()  + '</h2>' + newline  + newline        
        for dg in self.solution_registry_list:
            self.document_html = self.document_html + dg.output_html() + newline 
        self.document_html =  '<html>'  + self.document_html   + newline  + '</html>'          
        return self.document_html
   
    def get_dataframe(self):  
        import pandas as pd 
        row_number = -1
        df = pd.DataFrame(columns = ('solution_registry', 'solution_description'))
        for dg in self.solution_registry_list:
            row_number += 1  
            df.loc[row_number] = [dg.get_item(),dg.get_description()]
        return df 
    
    def erase_list(self):
        self.solution_registry_list = []     
    
    def reset_to_dataframe(self, reset_df):  
        import pandas as pd 
        self.erase_list()  
        for index, row in reset_df.iterrows():
            self.solution_registry_list.append(solution_registry(row[0],row[1])) 
    
    def read_from_file(self):
        import pandas as pd 
        import configparser 
        solution_name = 'solution_registry' 
        config = configparser.ConfigParser() 
        cfg = config.read('config.ini')  
        read_file_name = config.get('global_infrastructure', 'infrastructure_root_directory') + '/'  + \
        config.get('global_infrastructure', 'excel_subdirectory') + '/'  +  solution_name +  \
        config.get('global_infrastructure', 'excel_extension')
        df = pd.read_excel(read_file_name)        
        return df 
    
    def write_html_file(self, output_html_file_name):
        with open(output_html_file_name, 'w') as html_file:
            html_file.write(self.output_html())
            
    def add_to_list(self, item_name, item_description):
        self.solution_registry_list.append(solution_registry(item_name,item_description)) 
        
    def remove_from_list(self, item_name):
        self.solution_registry_list.remove(item_name)   
                 
    def write_document_file(self, output_document_file_name):
        with open(output_document_file_name, 'w') as document_file:
            document_file.write(self.output())                

    
        

                
