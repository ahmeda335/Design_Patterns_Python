from logger import Logger

class Debug:
    def __init__(self):
        self.logger = Logger
        
    def log(self):
        self.logger.log('Debug', 'Debugging required')