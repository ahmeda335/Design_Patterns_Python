from .Computer import Computer

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
        
        
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self   # I return self to can use chaining 
                    # builder.set_cpu('intel i9').set_gpu('RTX 4090')
        
    def set_ram(self, ram):
        self.computer.ram = ram
        return self
        
    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self
        
    def set_storage(self, storge):
        self.computer.storage = storge
        return self
        
    def set_power_supply(self, power_supply):
        self.computer.power_supply = power_supply
        return self
        
    def set_os(self, os):
        self.computer.os = os
        return self
    
    def build(self):
        return self.computer
        
        