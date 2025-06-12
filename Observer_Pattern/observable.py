from observers import IObserver

class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None
        
    def add_observer(self, observer: IObserver):
        self._observers.append(observer)
        
    def remove_observer(self, observer: IObserver):
        self._observers.remove(observer)
        
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)
        
    def set_temperature(self, temp):
        print(f"[WeatherStation] New temperature set: {temp}°C")
        self._temperature = temp
        self.notify_observers()