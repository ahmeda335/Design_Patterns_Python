# Flyweight Design Pattern - Tree Example 🌲

## Overview

This project demonstrates the **Flyweight Design Pattern** using a forest of trees where the intrinsic properties (like tree type) are shared to minimize memory usage, while the extrinsic properties (like tree position) are stored outside the shared object.

The Flyweight pattern is useful when you need to create a large number of similar objects and want to reduce memory consumption by sharing common parts of state.

---

## Structure

### 🧱 Classes

- **`Tree`**
  - Represents the flyweight object.
  - Holds **intrinsic** property: `tree_type`.
  - Has a method `render(x, y)` to simulate drawing the tree at given coordinates.

- **`TreeFactory`**
  - A factory that manages the flyweight instances.
  - Returns a shared `Tree` instance for the same `tree_type`.
  - Tracks and limits the number of unique tree types.

---

## Example Usage

```python
from tree_factory import TreeFactory

positions = [(10, 20), (15, 25), (20, 30), (10, 22), (17, 26)]
types = ["oak", "pine", "oak", "oak", "pine"]

for t, pos in zip(types, positions):
    tree = TreeFactory.get_tree(t)
    tree.render(*pos)

print(f"Total distinct tree types created: {TreeFactory.get_count()}")
```

### 🧾 Output
```
Rendering oak at (10, 20)
Rendering pine at (15, 25)
Rendering oak at (20, 30)
Rendering oak at (10, 22)
Rendering pine at (17, 26)
Total distinct tree types created: 2
```

---

## 🧠 Key Concepts

- **Intrinsic State**: Shared data (e.g., `tree_type`) stored in the flyweight object.
- **Extrinsic State**: Data unique per use (e.g., position) passed from outside.

---

## Benefits

✅ Reduces memory usage by sharing objects.  
✅ Improves performance in systems with many repeated objects.  
✅ Separates shared state from variable state.

---

## When to Use

- When you need to create a large number of objects.
- When object creation is expensive and can be optimized via sharing.
- When objects have many similar parts.

---

