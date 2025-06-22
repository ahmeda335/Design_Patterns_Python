from abc import ABCMeta, abstractmethod

class PaymentInterface(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def pay():
        "This function must be applied on all payment methods."