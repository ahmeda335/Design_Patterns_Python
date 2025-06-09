from abc import ABCMeta, abstractmethod
from copy import deepcopy, copy

class ICharacter(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def clone():
        "The is the function of cloning"
        
        
class Character(ICharacter):
    def __init__(self, health, strength, magic, weapon):
        self.health = health
        self.strength = strength
        self.magic = magic
        self.weapon = weapon
        
    def clone(self, mode=1):
        # Shallow Assignment
        if mode == 1:
            return self
        elif mode == 2:
            return copy(self)
        elif mode == 3:
            return deepcopy(self)
        else:
            raise ValueError("Invalid mode. Use 1 (ref), 2 (shallow), or 3 (deep).")
            
    def __str__(self):
        return f"""
            health: {self.health}
            strength: {self.strength}
            magic : {self.magic}
            weapon: {self.weapon}
        """
        