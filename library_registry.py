class library_registry(object):
    
    def __init__(self, library_registry, library_registry_description):
        self.library_registry = library_registry
        self.library_registry_description = library_registry_description

    def output(self):
        return ' {} {} '.format(self.library_registry, self.library_registry_description)
    
    def get_item(self):
        return self.library_registry
    
    def get_description(self):
        return self.library_registry_description    
    
    def output_html(self):
        return ' <li><b> {} </b> {}  </li>'.format(self.library_registry, self.library_registry_description)    
                                
class library_registry_list(object):   
                                
    def __init__(self):
        self.library_registry_list = [] 
        self.compose_library_registry()
        self.document = self.output() 

    def compose_library_registry(self):
        self.library_registry_list.append(library_registry('OS','The OS python library provides a portable way of using operating system dependent functionality to allow your python code to run on all platforms.')) 
        self.library_registry_list.append(library_registry('pyttsx3','pyttsx3 is a text-to-speech conversion library in Python that works offline.')) 
        self.library_registry_list.append(library_registry('ConfigParser','ConfigParser is used to implement a configuration settings.'))    
        self.library_registry_list.append(library_registry('Openpyxl','A library for reading and writing Excel files. The module also allows direct modification of Excel files.'))  
        self.library_registry_list.append(library_registry('glob','The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order.'))   
        self.library_registry_list.append(library_registry('time','The time module enables working with time.'))    
        self.library_registry_list.append(library_registry('datetime','The datetime module enables working with dates and times.'))     
        self.library_registry_list.append(library_registry('PyArrow','The PyArrow library provides a Python API for the functionality provided by the Apaches Arrow libraries')) 
        self.library_registry_list.append(library_registry('PANDAS','Pandas is a fast, powerful, flexible and easy to use open source data annalysis and  manipulation tool, built on top of the Python programming language.'))           
        self.library_registry_list.append(library_registry('SQLAlchemy','SQLAlchemy is a database toolkit and object-relational mapping (ORM) system for the Python programming language, first introduced in 2005.'))  
        self.library_registry_list.append(library_registry('NumPy','NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.'))  
        self.library_registry_list.append(library_registry('fastparquet','fastparquet is a python library for implementation of the parquet format, aiming integrate into python-based big data work-flows.'))     
        self.library_registry_list.append(library_registry('Pathlib','Pathlib is a native Python library for handling files and paths on your operating system.'))                                                           
                                                       
        
    def get_list_intro(self):  
        return('The registry of libraries are :') 
    
    def get_header(self):  
        return('Registry of Libraries')     
    
    def output(self):  
        newline = '\n'
        self.document = self.get_list_intro() + newline 
        for gt in self.library_registry_list:
            self.document = self.document + gt.output() + newline 
        return   self.document  
    
    def output_html(self):  
        newline = '\n'
        self.document_html = ''
        self.document_html =  self.document_html + newline + '<h1>'  + self.get_header() + '</h1>' +  newline 
        self.document_html =  self.document_html + newline + '<h2>' + self.get_list_intro()  + '</h2>' + newline  + newline        
        for gt in self.library_registry_list:
            self.document_html = self.document_html + gt.output_html() + newline 
        self.document_html =  '<html>'  + self.document_html   + newline  + '</html>'          
        return self.document_html
    
    def append_item(self, item_name, item_description):  
        self.library_registry_list.append(library_registry(item_name, item_description))         
    
    def output(self):  
        newline = '\n'
        self.document = self.get_list_intro() + newline 
        for dg in self.library_registry_list:
            self.document = self.document + dg.output() + newline 
        return   self.document  
    
    def output_html(self):  
        newline = '\n'
        self.document_html = ''
        self.document_html =  self.document_html + newline + '<h1>'  + self.get_header() + '</h1>' +  newline 
        self.document_html =  self.document_html + newline + '<h2>' + self.get_list_intro()  + '</h2>' + newline  + newline        
        for dg in self.library_registry_list:
            self.document_html = self.document_html + dg.output_html() + newline 
        self.document_html =  '<html>'  + self.document_html   + newline  + '</html>'          
        return self.document_html
   
    def get_dataframe(self):  
        import pandas as pd 
        row_number = -1
        df = pd.DataFrame(columns = ('registered_library', 'registered_library_description'))
        for dg in self.library_registry_list:
            row_number += 1  
            df.loc[row_number] = [dg.get_item(),dg.get_description()]
        return df 
    
    def erase_list(self):
        self.library_registry_list = []     
    
    def reset_to_dataframe(self, reset_df):  
        import pandas as pd 
        self.erase_list()  
        for index, row in reset_df.iterrows():
            self.library_registry_list.append(library_registry(row[0],row[1])) 
    
    def read_from_file(self):
        import pandas as pd 
        import configparser 
        solution_name = 'library_registry' 
        config = configparser.ConfigParser() 
        cfg = config.read('config.ini')  
        read_file_name = config.get('global_infrastructure', 'infrastructure_directory') + '/'  + \
        config.get('global_infrastructure', 'excel_directory') + '/'  +  solution_name +  \
        config.get('global_infrastructure', 'excel_extension')
        df = pd.read_excel(read_file_name)        
        return df 
    
    def write_html_file(self, output_html_file_name):
        with open(output_html_file_name, 'w') as html_file:
            html_file.write(self.output_html())
            
    def add_to_list(self, item_name, item_description):
        self.library_registry_list.append(library_registry(item_name,item_description)) 
        
    def remove_from_list(self, item_name):
        self.library_registry_list.remove(item_name)   
                 
    def write_document_file(self, output_document_file_name):
        with open(output_document_file_name, 'w') as document_file:
            document_file.write(self.output())                

    
        

                
