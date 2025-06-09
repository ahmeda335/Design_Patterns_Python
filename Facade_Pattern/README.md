# 🏠 Facade Design Pattern – Smart Home System

## 📌 Overview

The **Facade Design Pattern** provides a simplified interface to a complex subsystem. It hides the complexities of the underlying components and exposes a unified interface to the client.

In this example, we apply the pattern to a **Smart Home System**.

## 🎯 Problem

A smart home contains multiple subsystems:
- Light System
- Thermostat System
- Security System
- Music System

Interacting with each subsystem individually can be complex and repetitive. For example, to activate "Night Mode", you’d have to:
- Dim the lights
- Set a lower temperature
- Arm the security
- Stop the music

This isn't convenient for the user.

## ✅ Solution: Use a Facade

We create a `SmartHomeController` class that acts as a **facade**, providing simple methods like:

- `activate_night_mode()`
- `welcome_home()`
- `leave_home()`

Each method calls the necessary operations from the complex subsystems behind the scenes.

### 📦 Example Facade Usage

```python
controller = SmartHomeController()
controller.activate_night_mode()
