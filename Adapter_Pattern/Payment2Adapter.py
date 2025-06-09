from payment2 import Payment2


class Payment2Adapter:
    def __init__(self, amount):
        self.amount = amount
        self.payment2 = Payment2(self.amount)
        
    def pay(self):
        return self.payment2.make_payment()