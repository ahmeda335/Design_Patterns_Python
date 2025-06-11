from .. import IFactory
from .BMWVechiles import Car, Bike, Truck

class BMWFactory(IFactory):
    
    @staticmethod
    def get_vechile(vechile):
        try:
            if vechile == 'bmw car':
                return Car(), True
            elif vechile == 'bmw bike':
                return Bike(), True
            elif vechile == 'bmw truck':
                return Truck(), True
            else:
                return "No vechile found", False
        except:
            return "Error happened", False