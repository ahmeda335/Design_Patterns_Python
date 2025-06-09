from abc import ABC, abstractmethod

class FileSystemItem(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    @abstractmethod
    def display(self, indent=0):
        "Displaying the files"

    @abstractmethod
    @abstractmethod
    def get_size(self):
        "The size of the item"