from abc import ABCMeta, abstractmethod

class IVechile(metaclass=ABCMeta):
    "The vechiles interface"
    
    @staticmethod
    @abstractmethod
    def get_specs():
        """
        - A static interface method
        - This will be override by other vechiles
        """
        