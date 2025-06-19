from abc import ABCMeta, abstractmethod

class DataParser(metaclass=ABCMeta):
    def open_file(self, file):
        with open(file, 'r') as f:
            self.raw_data = f.read()
        return "File opened"
    
    @abstractmethod
    def load_data(self):
        pass
    
    def validate_data(self):
        pass
    
    @abstractmethod
    def extract_data(self):
        pass
    
    def close_file(self):
        self.raw_data = None
        self.data = None
        return "File closed"
    
    def parse(self, file):
        print("Opening File... ", self.open_file(file))
        print("Loading Data... ", self.load_data())
        print("Validating Data... ", self.load_data())
        print("Extracting Data... ", self.extract_data())
        print("Closing File... ", self.close_file())
    