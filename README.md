# 🎯 Design Patterns in Python

Welcome to my personal repository of **Design Patterns in Python** — a learning journey and implementation collection inspired by the book *"Design Patterns in Python"* 📘. Each folder in this repository contains one pattern, fully implemented with examples, use cases, and a detailed README for learning and reference.

---

## 🧱 Covered Patterns

### ✅ Creational Patterns
- **Factory** – Creates vehicles based on user input.
- **Abstract Factory** – Creates families of vehicles by brand (e.g., Toyota, BMW).
- **Builder** – Constructs complex computer configurations (Gaming or Office).
- **Prototype** – Clones character objects with optional shallow/deep copy.
- **Singleton** – Centralized logger accessed across multiple modules.

### 🎨 Structural Patterns
- **Decorator** – Dynamically adds formatting (bold, italic, color) to text messages.
- **Adapter** – Allows different payment systems (e.g., PayPal, Stripe) to work with a common interface.
- **Facade** – Simplifies user registration and payment through one unified interface.
- **Bridge** – Separates abstraction (remote controls) from implementation (TV/Radio).
- **Composite** – Represents a file system with files and folders in a tree structure.
- **Flyweight** – Shares tree types efficiently using a factory to save memory.
- **Proxy** – Controls access to a resource (e.g., secure file access) by acting as a substitute with additional permission checks.

### 📌Behavioral Patterns
- **Command** – Encapsulates requests (like turning lights on/off) as objects, allowing undo/redo and request queuing.
- **Chain of Responsibility** – Passes a request (e.g., ATM cash dispense) along a chain of handlers until one processes it.

---

## 📂 Project Structure

Each pattern is stored in its own folder:
```
/PatternName
│
├── core files (classes)
├── main.py (demo or test)
└── README.md (explanation and usage)
```

---

## 🎓 Purpose

This repository helps solidify understanding of **object-oriented design**, **code reusability**, and **separation of concerns** using design patterns. It’s a companion to the book and my own hands-on learning.

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/your-username/design-patterns-python.git
cd design-patterns-python
```

Run any example:

```bash
python Builder_Pattern/main.py
```

Each pattern is self-contained with a `main.py` script to demonstrate its usage.

---

## 🛠️ Tools Used

- Python 3.10+
- Standard Library Only (No external dependencies)

---

## 🙋 Why Design Patterns?

Design patterns are **proven solutions to common software design problems**. They make your code:

- More **maintainable**
- Easier to **extend**
- Easier for teams to **communicate**

---

## 📖 Reference

> *"Design Patterns in Python"* by Sean Bradley. Using GoF(Gang of Four).  
> Additional inspiration from:  
> - [Refactoring Guru](https://refactoring.guru/design-patterns)  
> - [SourceMaking](https://sourcemaking.com/design_patterns)

---

## 📬 Feedback

Feel free to fork, star ⭐, or submit pull requests to contribute or improve the examples.

---

## 📝 License

This repository is for **educational purposes** only.  
All code is open-source under the [MIT License](LICENSE).

