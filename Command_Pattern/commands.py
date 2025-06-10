from command_interface import Interface

class LightONCommand(Interface):
    def __init__(self, light):
        self._light = light
        
    def execute(self):
        self._light.turn_on()
        
        
        
class LightOFFCommand(Interface):
    def __init__(self, light):
        self._light = light
        
    def execute(self):
        self._light.turn_off()
        
        
class MusicONCommand(Interface):
    def __init__(self, music):
        self._music = music
        
    def execute(self):
        self._music.turn_on()
        
        
        
class MusicOFFCommand(Interface):
    def __init__(self, music):
        self._music = music
        
    def execute(self):
        self._music.turn_off()
        
        
class GarageOpenCommand(Interface):
    def __init__(self, garage):
        self._garage = garage
        
    def execute(self):
        self._garage.turn_on()
        
        
        
class GarageCloseCommand(Interface):
    def __init__(self, garage):
        self._garage = garage
        
    def execute(self):
        self._garage.turn_off()