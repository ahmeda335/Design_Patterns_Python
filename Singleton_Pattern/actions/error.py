from logger import Logger

class Error:
    def __init__(self):
        self.logger = Logger
        
    def log(self):
        self.logger.log('Error', 'Error happened with the action')