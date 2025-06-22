# Bridge Design Pattern

The **Bridge Pattern** is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—**abstraction** and **implementation**—which can be developed independently.

## 📚 Concept

In this example, we simulate remote controls for various devices such as TVs and Radios.

- **Abstraction:** `RemoteControl`
- **Implementation:** `Device` (e.g., `TV`, `Radio`, `Projector`)

This separation allows us to mix and match controls with devices without creating an explosion of subclasses.

---
## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have Python 3.6+ installed.
3. Run the main file using the command below:

```bash
python main.py
```

---

## 🧩 Structure

### Abstractions

- **RemoteControl**: The base abstraction for a remote control.

### Implementations

- **Device**: Interface for all concrete devices (`TV`, `Radio`)
- **TV**: Concrete device that supports basic functionalities.
- **Radio**: Another device implementation.

---

## 🕹️ Features

### RemoteControl (Basic)

- `turn_on()`
- `turn_off()`
- `set_channel(channel)`
- `volume_up()`
- `volume_down()`


## 🧪 Example

```python
tv = TV
remote = RemoteControl(tv)

remote.turn_on()
remote.set_channel(5)
remote.volume_up()
remote.turn_off()
