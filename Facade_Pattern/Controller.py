from Music_System import MusicSystem
from Security_System import SecuritySystem
from Lights_System import LightSystem
from Thermostat_System import ThermostatSystem

class Controller:
    def __init__(self):
        self.music = MusicSystem()
        self.security = SecuritySystem()
        self.lights = LightSystem()
        self.thermostat = ThermostatSystem()
        
    def activate_night_mode(self):
        self.lights.dim()
        self.thermostat.set_temperature(18)
        self.security.arm()
        self.music.stop()

    def welcome_home(self):
        self.lights.turn_on()
        self.thermostat.set_temperature(22)
        self.security.disarm()
        self.music.play()