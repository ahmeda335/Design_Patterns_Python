# Composite Design Pattern - File System Example 📁

## Overview

This project demonstrates the **Composite Design Pattern** by simulating a simple file system using `File` and `Folder` classes.

The Composite pattern lets you treat individual objects (`File`) and compositions of objects (`Folder`) uniformly. This is useful for building tree structures like a file system.

---

## Structure

### 🧩 Components

- **`IComponent`** (interface)
  - Common interface for all components.
  - Methods:
    - `add(component)` – Add a subcomponent (optional, only for folders).
    - `get_size()` – Returns the size of the component.
    - `display(indent=0)` – Displays the structure.

- **`File`** (Leaf)
  - Implements `IComponent`.
  - Represents a file with a name and size.
  - Does **not** support adding subcomponents.

- **`Folder`** (Composite)
  - Implements `IComponent`.
  - Can contain multiple `File` or `Folder` objects.
  - Can calculate total size of all its contents.
  - Supports recursive display.

---

## Example Usage

```python
from folder import Folder
from file import File

# Create files
file1 = File("resume.docx", 120)
file2 = File("budget.xlsx", 80)
file3 = File("photo.jpg", 250)

# Create folders
root = Folder("root")
documents = Folder("documents")
pictures = Folder("pictures")

# Build structure
documents.add(file1)
documents.add(file2)
pictures.add(file3)

root.add(documents)
root.add(pictures)

# Display structure
root.display()

# Get total size
print("Total size:", root.get_size(), "KB")
```

---

## 🧾 Output

```
📁 root
  📁 documents
    📄 resume.docx (120KB)
    📄 budget.xlsx (80KB)
  📁 pictures
    📄 photo.jpg (250KB)
Total size: 450 KB
```

---

## Key Concepts

- **Tree Structure**: You can represent hierarchies using folders and files.
- **Uniform Interface**: Both files and folders implement the same interface.
- **Recursive Operations**: `display()` and `get_size()` operate recursively.

---

## When to Use

- When your objects naturally form a **tree structure**, like:
  - File systems
  - Menus
  - Organization hierarchies
- When you want to treat **individual and composite objects uniformly**.

---

## Notes

❌ `remove()` is **not implemented** in this version, but can easily be added to `Folder` if needed.  
✅ Each class focuses on either being a leaf (`File`) or a container (`Folder`) without mixing responsibilities.

---
