from interface import IDispenser

class Dispenser50(IDispenser):
    def __init__(self):
        self._successor = None
        
    def next_successor(self, successor):
        self._successor = successor
        
    def handle(self, amount):
        if amount >= 50:
            num = amount // 50
            remainder = amount % 50
            print(f"Dispensing {num} $50 note(s)")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)