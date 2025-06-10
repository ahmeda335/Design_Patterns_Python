from abc import ABCMeta, abstractmethod

class Interface(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method that all command objects will use"