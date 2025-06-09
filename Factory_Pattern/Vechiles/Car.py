from .vechile import IVechile


class Car(IVechile):
    "This concrete class implements the vechile interface"
    
    def __init__(self):
        self._type = "Car"
        self._wheels = "Four"
        self._max_speed = 280
        self._prices_range = (200, 1500)
        
    def get_specs(self):
        return{
            "type": self._type,
            "Number of wheels": self._wheels,
            "Max Speed" : self._max_speed,
            "Prices Range": self._prices_range
        }