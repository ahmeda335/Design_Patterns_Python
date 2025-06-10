from abc import ABCMeta, abstractmethod

class IDispenser(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def next_successor(successor):
        "Set the next successor"
        
    @staticmethod
    @abstractmethod
    def handle(amount):
        "Handle the event"