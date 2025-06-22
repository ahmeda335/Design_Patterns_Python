class CareTaker:
    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def save(self):
        "Store a new memento for the text editor"
        print("CareTaker: Text saved.")
        memento = self._originator.memento
        self._mementos.append(memento)
        
    def restore(self, index):
        "Restoring a memento with its index."
        print("CareTaker: Restoring from Memento")
        memento = self._mementos[index]
        self._originator.memento = memento
        