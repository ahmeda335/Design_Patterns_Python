from abc import ABCMeta, abstractmethod

class IVisitable(metaclass=ABCMeta):
    """
    An interface that concrete objects should implement that allows 
    the visitor to traverse a hierarchical structure of objects
    """
    @staticmethod
    @abstractmethod
    def accept(visitor):
        """
        The visitor traverse and accesses each object through this mehtod.
        """