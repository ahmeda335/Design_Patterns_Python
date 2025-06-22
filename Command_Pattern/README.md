# 🧠 Command Design Pattern in Python

This project demonstrates the **Command Design Pattern**, one of the behavioral patterns described in the "Design Patterns in Python" book. The Command Pattern encapsulates a request as an object, thereby allowing for parameterization of clients with different requests, queuing of requests, and logging of the history.

---

## 📌 Concept

The **Command Pattern** decouples the object that invokes the operation from the one that knows how to perform it. It’s useful when you want to issue requests to objects without knowing anything about the operation being requested or the receiver of the request.

---

## 🏗️ Structure

- **Command Interface**: Declares the `execute()` and optionally `undo()` methods.
- **ConcreteCommand**: Implements the Command interface and defines a binding between a Receiver object and an action.
- **Receiver**: Knows how to perform the operations.
- **Invoker (Controller/RemoteControl)**: Stores command objects and triggers their execution.
- **Client**: Creates command objects and configures the invoker.

---
## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have Python 3.6+ installed.
3. Run the main file using the command below:

```bash
python main.py
```

---

## 🧱 Classes

- `Command` (interface/abstract class)
- `TurnOnLightCommand`, `TurnOffLightCommand`, etc. (concrete commands)
- `Light` (receiver)
- `RemoteControl` (invoker/controller)
- `main.py` (client)

---

## 📄 Example

```python
# Receiver
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

# Command Interface
class Command:
    def execute(self): pass
    def undo(self): pass

# Concrete Commands
class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class TurnOffLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Invoker (Controller)
class RemoteControl:
    def __init__(self):
        self._commands = {}
        self._last_command = None

    def set_command(self, button, command):
        self._commands[button] = command

    def press(self, button):
        if button in self._commands:
            self._commands[button].execute()
            self._last_command = self._commands[button]
        else:
            print("No command assigned.")


# Client
light = Light()
on_command = TurnOnLightCommand(light)
off_command = TurnOffLightCommand(light)

remote = RemoteControl()
remote.set_command("ON", on_command)
remote.set_command("OFF", off_command)

remote.press("ON")
remote.press("OFF")
remote.undo()
```

---

## ✅ Use Cases

- GUI button actions
- Macro recording
- Transactional operations (e.g., undo/redo systems)
- Remote control for home automation

---

## 📚 Source

Based on "Design Patterns in Python" book.
