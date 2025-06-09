from IText import IText

class ColorDecorator(IText):
    def __init__(self, value):
        self.color_value = f"\033[31m{value}\033[0m"   # RED
        
    def __str__(self):
        return str(self.color_value)