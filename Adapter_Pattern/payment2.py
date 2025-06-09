class Payment2:
    def __init__(self, amount):
        self.amount = amount
        
    def make_payment(self):
        print(f"You paid amount {self.amount}")