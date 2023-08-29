class glossary_term(object):

    def __init__(self, glossary_term, glossary_term_description):
        self.glossary_term = glossary_term
        self.glossary_term_description = glossary_term_description

    def output(self):
        return ' {} {} '.format(self.glossary_term, self.glossary_term_description)
    
    def output_html(self):
        return ' <li><b> {} </b> {}  </li>'.format(self.glossary_term, self.glossary_term_description)    
                                
class glossary_of_term_list(object):   
                                
    def __init__(self):
        self.glossary_term_list = [] 
        self.compose_glossary_term()
        self.document = self.output() 

    def compose_glossary_term(self):
        self.glossary_term_list.append(glossary_term('PYTHON','Python is a general-purpose programming language widely used for data science.')) 
        self.glossary_term_list.append(glossary_term('SQL','Structured Query Language(SQL) is commonly used for manipulating and querying data.'))  
        self.glossary_term_list.append(glossary_term('CSV','A Comma-Separated Values(CSV) is a text file in which data is separated by commas.'))  
        self.glossary_term_list.append(glossary_term('SECURITY','To secure the solution and data is only available to those who have appropriate access.')) 
        self.glossary_term_list.append(glossary_term('PERFORMANT','The solution performs quickly enough to meet the business demand.'))  
        self.glossary_term_list.append(glossary_term('Magic or Dunder Methods','Magic methods in Python are the special methods that start and end with the double underscores. They are also called dunder methods. Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action.')) 
       
        
    def get_list_intro(self):  
        return('The Glossary of Terms are :') 
    
    def get_header(self):  
        return('Glossary of Terms')    
    
    def append_item(self, glossary_term, glossary_term_description):  
        self.glossary_term_list.append(glossary_term(glossary_term, glossary_term_description)) 
    
    def output(self):  
        newline = '\n'
        self.document = self.get_list_intro() + newline 
        for gt in self.glossary_term_list:
            self.document = self.document + gt.output() + newline 
        return   self.document  
    
    def output_html(self):  
        newline = '\n'
        self.document_html = ''
        self.document_html =  self.document_html + newline + '<h1>'  + self.get_header() + '</h1>' +  newline 
        self.document_html =  self.document_html + newline + '<h2>' + self.get_list_intro()  + '</h2>' + newline  + newline        
        for gt in self.glossary_term_list:
            self.document_html = self.document_html + gt.output_html() + newline 
        self.document_html =  '<html>'  + self.document_html   + newline  + '</html>'          
        return self.document_html
    
    def write_html_file(self, output_html_file_name):
        self.html_file_name = 'glossary_of_terms.html'   # the default HTML file name to write too 
        if len(output_html_file_name) > 2: 
            self.html_file_name = output_html_file_name
        with open(self.html_file_name, 'w') as html_file:
            html_file.write(self.output_html())
                  
    def write_document_file(self, output_document_file_name):
        document_file_name = 'glossary_of_terms_document.doc'   # the default document_file_name file name to write too 
        if len(output_document_file_name) > 2: 
            file_name = output_document_file_name
        with open(file_name, 'w') as document_file:
            document_file.write(self.output())                   
                  
