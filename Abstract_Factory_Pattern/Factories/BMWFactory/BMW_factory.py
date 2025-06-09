from ..factory import IFactory
from .BMWVechiles.Car import Car
from .BMWVechiles.Bike import Bike
from .BMWVechiles.Truck import Truck

class BMWFactory(IFactory):
    
    @staticmethod
    def get_vechile(vechile):
        try:
            if vechile == 'bmw car':
                return Car()
            elif vechile == 'bmw bike':
                return Bike()
            elif vechile == 'bmw truck':
                return Truck()
            else:
                return "No vechile found"
        except:
            return "Error happened"