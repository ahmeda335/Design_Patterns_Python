from .Interface import PaymentInterface


class PayPalPayment(PaymentInterface):
    def __init__(self, amount):
        self.amount = amount
        
    def pay(self):
        return f"Paypal Payment Successful   -->   {self.amount}$"
