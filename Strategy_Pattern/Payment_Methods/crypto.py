from .Interface import PaymentInterface


class CryptoPayment(PaymentInterface):
    def __init__(self, amount):
        self.amount = amount
        
    def pay(self):
        return f"Crypto Payment Successful   -->  {self.amount}$"    
    
    __call__ = pay
