from ..factory import IFactory
from .ToyotaVechiles.Car import Car
from .ToyotaVechiles.Bike import Bike
from .ToyotaVechiles.Truck import Truck

class ToyotaFactory(IFactory):
    
    @staticmethod
    def get_vechile(vechile):
        try:
            if vechile == 'toyota car':
                return Car(), True
            elif vechile == 'toyota bike':
                return Bike(), True
            elif vechile == 'toyota truck':
                return Truck(), True
            else:
                return "No vechile found", False
        except:
            return "Error happened", False
        