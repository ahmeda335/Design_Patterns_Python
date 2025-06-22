class Mediator:
    def __init__(self):
        self._colleagues = {}

    def send_message(self, sender, message):
        print(f"[ChatRoom] {sender.alias} sends: {message}")
        for alias in self._colleagues:
            if alias != sender.alias:
                self._colleagues[alias].notify(message)
    
    def add_student(self, student):
        self._colleagues[student.alias] = student
        
    def show_students(self):
        for alias in self._colleagues:
            print(alias)
