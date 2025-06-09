from IText import IText

class BoldDecorator(IText):
    def __init__(self, value):
        self.bold_value = f"\033[1m{value}\033[0m"
        
    def __str__(self):
        return str(self.bold_value)