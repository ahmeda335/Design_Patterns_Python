class RemoteControl:
    def __init__(self, device):
        self.device = device()
        
    def turn_on(self):
        self.device.turn_on()
        
    def turn_off(self):
        self.device.turn_off()
        
    def set_channel(self, channel):
        self.device.set_channel(channel)
        
    def volume_up(self):
        self.device.volume_up()
        
    def volume_down(self):
        self.device.volume_down()