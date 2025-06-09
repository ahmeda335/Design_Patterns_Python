class Payment1:
    def __init__(self, amount):
        self.amount = amount
        
    def pay(self):
        print(f"You paid amount {self.amount}")