from memento import Memento

class TextEditor:
    def __init__(self):
        self._text = ''

    def write(self, text):
        self._text = text
        
    @property
    def memento(self):
        "Getter function for this version of text as Memento"
        return Memento(self._text)
    
    @memento.setter
    def memento(self, memento: Memento):
        "Setter function"
        self._text = memento.text
        
    def __str__(self):
        return self._text
    