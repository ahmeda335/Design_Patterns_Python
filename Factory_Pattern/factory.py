from Vechiles.Car import Car
from Vechiles.Bike import Bike
from Vechiles.Truck import Truck


class Factory:
    @staticmethod
    def get_vechile(vechile):
        try:
            if vechile == 'car':
                return Car()
            elif vechile == 'bike':
                return Bike()
            elif vechile == 'truck':
                return Truck()
            else:
                return "No vechile found"
        except:
            return "Error happened"
        