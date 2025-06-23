from number import Number

class Add:
    def __init__(self, left: Number, right: Number):
        self.left = left
        self.right = right
        
    def interpret(self):
        return self.left.interpret() + self.right.interpret()
    
    def __repr__(self):
        return f"({self.left} Add {self.right})"
    
    
class Subtract:
    def __init__(self, left: Number, right: Number):
        self.left = left
        self.right = right
        
    def interpret(self):
        return self.left.interpret() - self.right.interpret()
    
    def __repr__(self):
        return f"({self.left} Subtract {self.right})"
    