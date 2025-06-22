from .Interface import PaymentInterface


class CreditCardPayment(PaymentInterface):
    def __init__(self, amount):
        self.amount = amount
        
    def pay(self):
        return f"Credit Card Payment Successful   -->  {self.amount}$"
    