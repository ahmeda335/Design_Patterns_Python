from abc import abstractmethod, ABCMeta

class IText(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def __str__():
        "This will be override by both the text and its decorators"