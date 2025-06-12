# 🌦️ Weather Station - Observer Design Pattern in Python

This is a Python implementation of the **Observer Design Pattern** using a weather station as the example scenario.

The **Weather Station** (Subject) notifies multiple display devices (Observers) whenever the temperature changes.

## 🧠 Design Pattern Overview

The **Observer Pattern** allows objects (observers) to subscribe to another object (subject) and get automatically notified when the subject’s state changes. It promotes loose coupling and is useful for event-driven programming.

### Participants

- **Subject**: `WeatherStation`
- **Observer Interface**: `Observer`
- **Concrete Observers**: `PhoneDisplay`, `LaptopDisplay`

## 🚀 How to Run

Run main.py