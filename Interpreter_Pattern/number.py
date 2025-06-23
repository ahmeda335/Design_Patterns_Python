class Number:
    def __init__(self, value):
        self.value = int(value)
        
    def interpret(self):
        return self.value
    
    def __repr__(self):
        return str(self.value)
        