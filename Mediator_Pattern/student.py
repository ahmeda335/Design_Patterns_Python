class Student:
    def __init__(self, alias):
        self.alias = alias
        
    def notify(self, message):
        print(f"{self.alias} receives message: {message}")
