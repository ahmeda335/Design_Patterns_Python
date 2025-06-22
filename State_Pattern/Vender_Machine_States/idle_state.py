from .interface import StatesInterface

class IdleState(StatesInterface):
    
    def __init__(self, money):
        self.money = money
        print(f"{self.money}$ inserted..")
    