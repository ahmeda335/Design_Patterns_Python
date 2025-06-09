from .vechile import IVechile


class Truck(IVechile):
    "This concrete class implements the vechile interface"
    
    def __init__(self):
        self._type = "Truck"
        self._wheels = "Eight"
        self._max_speed = 220
        self._prices_range = (1200, 4000)
        
    def get_specs(self):
        return{
            "type": self._type,
            "Number of wheels": self._wheels,
            "Max Speed" : self._max_speed,
            "Prices Range": self._prices_range
        }