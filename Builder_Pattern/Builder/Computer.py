class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None
        self.power_supply = None
        self.os = None
        
    def construction(self):
        "Returning a string descriping the computer"
        return f"""The computer has specs
                    CPU: {self.cpu}
                    GPU: {self.gpu}
                    RAM: {self.ram}
                    STORAGE: {self.storage}
                    POWER SUPPLY: {self.power_supply}
                    OPERATING SYSTEM: {self.os}
                    """