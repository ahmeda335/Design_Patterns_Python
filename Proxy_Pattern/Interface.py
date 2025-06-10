from abc import ABCMeta, abstractmethod

class Document(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def display():
        "Display the document"