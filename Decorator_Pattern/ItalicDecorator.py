from IText import IText

class ItalicDecorator(IText):
    def __init__(self, value):
        self.italic_value = f"\033[3m{value}\033[0m"
        
    def __str__(self):
        return str(self.italic_value)