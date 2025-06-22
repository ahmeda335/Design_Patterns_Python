from .interface import StatesInterface


class DispensingState(StatesInterface):
    def __init__(self):
        print("Take your money.")
        