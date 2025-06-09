# Singleton Design Pattern – Logger Example

This project demonstrates the **Singleton Design Pattern** in Python using a centralized `Logger` class. Multiple components of the application (`success`, `error`, `debug`, and `authenticate`) log messages through a single shared instance of the `Logger`.

---

## 📌 Design Pattern: Singleton

- Ensures a class has **only one instance** and provides a global point of access to it.
- Used here to maintain **one shared logger** across the entire application.