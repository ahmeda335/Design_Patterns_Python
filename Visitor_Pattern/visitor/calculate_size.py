from .visitor_interface import IVisitor

class SizeCalculatorSize(IVisitor):
    def __init__(self):
        self.total_size = 0

    def visit(self, element):
        if hasattr(element, 'size'):
            self.total_size += element.size
            
        return self.total_size
