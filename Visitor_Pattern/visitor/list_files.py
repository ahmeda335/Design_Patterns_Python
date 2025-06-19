from .visitor_interface import IVisitor


class FileListVisitor(IVisitor):
    def __init__(self):
        self.elements = []
        
    def visit(self, element):
        self.elements.insert(0, element.name)
    