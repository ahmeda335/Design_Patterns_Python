from Interface import Document


class RealDocument(Document):
    def __init__(self, form_name):
        self.form_name = form_name
        self.load()
        
    def display(self):
        print(f"Displaying the document {self.form_name}")
        
    def load(self):
        print(f"Loading the form {self.form_name}")