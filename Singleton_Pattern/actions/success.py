from logger import Logger

class Success:
    def __init__(self):
        self.logger = Logger
        
    def log(self):
        self.logger.log('Success', 'The action is successful')