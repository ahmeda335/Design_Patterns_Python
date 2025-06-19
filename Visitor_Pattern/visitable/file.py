from .visitable_interface import IVisitable
from visitor import IVisitor
from .directory import Directory

class File(IVisitable):
    def __init__(self, name, size, extension, parent: Directory = None):
        self.name = name
        self.size = size
        self.extension = extension
        if parent:
            parent.elements.add(self)
            
    def accept(self, visitor: IVisitor):
        visitor.visit(self)