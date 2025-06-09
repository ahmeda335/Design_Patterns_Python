from abc import ABCMeta, abstractmethod

class IFactory(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def get_vechile():
        "A static interface method"