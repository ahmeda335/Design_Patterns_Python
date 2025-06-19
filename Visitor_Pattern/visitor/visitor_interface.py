from abc import ABCMeta, abstractmethod

class IVisitor(metaclass=ABCMeta):
    "An interface that custom visitors should implement"
    
    def visit_file(file):
        "Visitors visit the files within the app"
        
    def visit_directory(directory):
        "Visitors visit the directories within the app"
