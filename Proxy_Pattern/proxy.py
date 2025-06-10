from Interface import Document
from real_document import RealDocument

class DocumentProxy(Document):
    def __init__(self, form_name, user):
        self.form_name = form_name
        self.user = user
        self.form = None
        
    def display(self):
        if self.user == 'admin':
            if self.form is None:
                print("Loading from Real Document")
                self.form = RealDocument(self.form_name)
                self.form.display()
            else:
                print("Loading from Proxy")
                self.form.display()
                
        else:
            print(f"You are unauthorized to see this document.")
            