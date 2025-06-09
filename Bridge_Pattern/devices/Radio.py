from .device import IDevice

class Radio(IDevice):
    def turn_on(self):
        print("Radio is now ON")

    def turn_off(self):
        print("Radio is now OFF")

    def set_channel(self, frequency):
        print(f"Radio tuned to {frequency} MHz")

    def volume_up(self):
        print("Radio volume increased")

    def volume_down(self):
        print("Radio volume decreased")
