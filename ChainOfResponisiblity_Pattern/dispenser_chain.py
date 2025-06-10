from dispenser1 import Dispenser50
from dispenser2 import Dispenser100
from dispenser3 import Dispenser200


class ATMDispenserChain:
    def __init__(self):
        self.chain1 = Dispenser200()
        self.chain2 = Dispenser100()
        self.chain3 = Dispenser50()
        
        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)