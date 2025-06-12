from abc import ABCMeta, abstractmethod

class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def update(temperature):
        "Updating the temperatures in the observers"


class PhoneDisplay(IObserver):
    def update(self, temperature):
        print(f"[PhoneDisplay] Temperature updated to {temperature}°C")


class LaptopDisplay(IObserver):
    def update(self, temperature):
        print(f"[LaptopDisplay] Temperature updated to {temperature}°C")