from .visitor_interface import IVisitor

class ExtensionCounterVisitor(IVisitor):
    extensions = {}
    
    @classmethod
    def visit(cls, element):
        if hasattr(element, 'extension'):
            if element.extension in cls.extensions.keys():
                cls.extensions[element.extension] += 1
            else:
                cls.extensions[element.extension] = 1     
        
        return cls.extensions