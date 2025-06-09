from .device import IDevice

class TV(IDevice):
    def turn_on(self):
        print("TV is now ON")

    def turn_off(self):
        print("TV is now OFF")

    def set_channel(self, channel):
        print(f"TV channel set to {channel}")

    def volume_up(self):
        print("TV volume increased")

    def volume_down(self):
        print("TV volume decreased")
