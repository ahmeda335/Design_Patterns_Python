from .device import IDevice

class Projector(IDevice):
    def turn_on(self):
        print("Projector is now ON")

    def turn_off(self):
        print("Projector is now OFF")

    def set_channel(self, input_source):
        print(f"Projector input source set to {input_source}")

    def volume_up(self):
        print("Projector speaker volume increased")

    def volume_down(self):
        print("Projector speaker volume decreased")
