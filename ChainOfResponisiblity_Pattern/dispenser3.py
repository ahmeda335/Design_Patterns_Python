from interface import IDispenser

class Dispenser200(IDispenser):
    def __init__(self):
        self._successor = None
        
    def next_successor(self, successor):
        self._successor = successor
        
    def handle(self, amount):
        if amount >= 200:
            num = amount // 200
            remainder = amount % 200
            print(f"Dispensing {num} $200 note(s)")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)