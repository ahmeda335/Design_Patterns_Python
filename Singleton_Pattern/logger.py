class Logger:
    logs = {}  # This is a class level variable.
    
    def __new__(cls):
        return cls
    
    @classmethod
    def log(cls, action, message):
        cls.logs[action] = message
    
    @staticmethod 
    def get_logs(cls):
        return cls.logs