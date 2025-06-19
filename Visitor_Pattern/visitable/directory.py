from .visitable_interface import IVisitable
from visitor import IVisitor

class Directory(IVisitable):
    def __init__(self, name, parent = None):
        self.name = name
        self.elements = set()
        if parent:
            parent.elements.add(self)
        
    def accept(self, visitor: IVisitor):
        for element in self.elements:
            element.accept(visitor)
        visitor.visit(self)