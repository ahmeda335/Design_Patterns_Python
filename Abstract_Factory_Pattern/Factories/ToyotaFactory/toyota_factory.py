from ..factory import IFactory
from .ToyotaVechiles.Car import Car
from .ToyotaVechiles.Bike import Bike
from .ToyotaVechiles.Truck import Truck

class ToyotaFactory(IFactory):
    
    @staticmethod
    def get_vechile(vechile):
        try:
            if vechile == 'toyota car':
                return Car()
            elif vechile == 'toyota bike':
                return Bike()
            elif vechile == 'toyota truck':
                return Truck()
            else:
                return "No vechile found"
        except:
            return "Error happened"
        