from .vechile import IVechile


class Bike(IVechile):
    "This concrete class implements the vechile interface"
    
    def __init__(self):
        self._brand = "BMW"
        self._type = "Bike"
        self._wheels = "Two"
        self._max_speed = 120
        self._prices_range = (40, 300)
        
    def get_specs(self):
        return{
            "brand": self._brand,
            "type": self._type,
            "Number of wheels": self._wheels,
            "Max Speed" : self._max_speed,
            "Prices Range": self._prices_range
        }