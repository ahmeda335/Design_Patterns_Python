from abc import ABCMeta, abstractmethod


class IDevice(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def turn_on():
        "This will be override"
        
    @staticmethod
    @abstractmethod
    def turn_off():
        "This will be override"
        
    @staticmethod
    @abstractmethod
    def set_channel():
        "This will be override"
        
    @staticmethod
    @abstractmethod
    def volume_up():
        "This will be override"
        
    @staticmethod
    @abstractmethod
    def volume_down():
        "This will be override"
        
    