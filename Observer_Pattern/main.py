from observers import PhoneDisplay, LaptopDisplay
from observable import WeatherStation

station = WeatherStation()

phone = PhoneDisplay()
laptop = LaptopDisplay()

station.add_observer(phone)
station.add_observer(laptop)

station.set_temperature(25)
station.set_temperature(40)