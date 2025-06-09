from logger import Logger

class Authenticate:
    def __init__(self):
        self.logger = Logger
        
    def log(self):
        self.logger.log('Authenticate', 'Authentication is required')