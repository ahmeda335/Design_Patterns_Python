from Vender_Machine_States import StatesInterface, IdleState, HasMoneyState, DispensingState


class Context():
    
    def __init__(self, money):
        self.money = money
        self.state_handles = [
            IdleState(self.money),
            HasMoneyState(),
            DispensingState(),
        ]
        self._handle = iter(self.state_handles)
        
    def request(self):
        "Each time the request is called, a new class will handle it."
        try:
            self.handle.__next__()()
        except StopIteration:
            self._handle = iter(self.state_handles)
