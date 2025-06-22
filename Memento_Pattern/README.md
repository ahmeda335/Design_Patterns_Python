# 📝 Text Editor – Memento Design Pattern in Python

This project demonstrates the **Memento Design Pattern** using a simple text editor that supports writing and undoing text. The pattern is useful when you need to capture and restore the internal state of an object without violating encapsulation.

## 🧠 Design Pattern Overview

The **Memento Pattern** captures and stores an object’s internal state so it can be restored later. It’s commonly used to implement features like undo, history, snapshots, and version control.

## 💡 Use Case: Simple Text Editor with Undo

The user can:
- Write text.
- Save the current state.
- Undo to a previous version of the text.

## 🧱 Components

- **Originator**: `TextEditor`  
  Contains the current content of the editor. Can create and restore mementos representing its state.

- **Memento**: `EditorMemento`  
  Stores the state (text content) of the editor. Only accessible by the `TextEditor`.

- **Caretaker**: `HistoryManager`  
  Maintains a history (stack/list) of `EditorMemento` objects. Manages undo functionality by restoring previous states.

## 🚀 How to Run

1. Ensure Python 3.6+ is installed.
2. Run the main script:

```bash
python main.py
```