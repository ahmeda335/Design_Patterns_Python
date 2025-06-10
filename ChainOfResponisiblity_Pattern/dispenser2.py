from interface import IDispenser

class Dispenser100(IDispenser):
    def __init__(self):
        self._successor = None
        
    def next_successor(self, successor):
        self._successor = successor
        
    def handle(self, amount):
        if amount >= 100:
            num = amount // 100
            remainder = amount % 100
            print(f"Dispensing {num} $100 note(s)")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)