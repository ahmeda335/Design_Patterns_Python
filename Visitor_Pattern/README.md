# 🧭 Visitor Design Pattern – File System Example (Python)

This project demonstrates the **Visitor Design Pattern** through a simple hierarchical **file system** structure containing `Directory` and `File` objects.

The Visitor Pattern is used to perform different operations (like listing files, calculating size, etc.) on a structure of objects without modifying their classes.

---

## 🚀 How to Run

To test the visitor pattern and see it in action, simply run the `main.py` file:

```bash
python main.py
```

This will:

- Build a sample file system with nested directories and files

Make sure all modules (like `directory`, `file`, and `visitor`) are in the correct folders and properly imported.

---

## 📁 Structure

- **Directory**: Can contain other directories and files.
- **File**: Has attributes like name, size, and extension.
- **Visitors**:
  - `FileListVisitor`: Collects names of all files and directories.
  - `ExtensionCounterVisitor' : Collects the extensions found and the number of each.
  - `SizeCalculatorSize`: Calculate the size of all the files in the directories.

---

## 🔧 Components

- `IVisitable`: Interface for elements that accept visitors.
- `IVisitor`: Interface for all visitor classes.
- `Directory`: Implements `accept(visitor)` and holds child elements.
- `File`: Implements `accept(visitor)`.
- `FileListVisitor`: Implements `visit(element)` to collect names.
  - `ExtensionCounterVisitor' : Implements `visit(element)` to get extensions.
  - `SizeCalculatorSize`: Implements `visit(element)` to get the total size.

---


## ✅ How It Works

- Each `Directory` or `File` implements `accept(visitor)` and calls `visitor.visit(self)`.
- The `Directory.accept()` visits itself first (pre-order), then passes the visitor to its children.
- `FileListVisitor` collects elements into a list for later inspection or printing.

---

## 📦 Extendable

You can easily add new operations by implementing new visitors:
- `SizeCalculatorVisitor`
- `ExtensionCounterVisitor`
- `TreeViewPrinterVisitor`

No need to modify the `Directory` or `File` classes!

---

## 🧠 Benefits of Visitor Pattern

- Open/Closed Principle: Add new behaviors without changing element classes.
- Clean separation between structure and operations.
- Simplifies complex traversals.

---

## 📝 Author

Made for educational purposes to demonstrate the **Visitor Design Pattern** in Python.
