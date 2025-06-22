## 🖋️ Text Formatting in Python

This project demonstrates how to format text with **bold**, *italic*, and 🎨 colors in Python.

---

---
## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have Python 3.6+ installed.
3. Run the main file using the command below:

```bash
python main.py
```

### ✅ Console / Terminal Formatting (Using ANSI Escape Codes)

You can style text output in the terminal using ANSI escape codes.

#### 🔹 Bold Text
```python
print("\033[1mThis is bold text\033[0m")
```

#### 🔹 Italic Text
```python
print("\033[3mThis is italic text\033[0m")
```
> Note: Italic may not be supported in all terminals.

#### 🔹 Colored Text (Example: Red)
```python
print("\033[31mThis is red text\033[0m")
```

#### 🎨 Common ANSI Color Codes

| Color   | Code |
|---------|------|
| Black   | 30   |
| Red     | 31   |
| Green   | 32   |
| Yellow  | 33   |
| Blue    | 34   |
| Magenta | 35   |
| Cyan    | 36   |
| White   | 37   |

> Always reset the formatting with `\033[0m` after your styled text.

---

### ✅ Markdown Formatting (For Docs Only)

Markdown supports:

- **Bold** → `**bold**`
- *Italic* → `*italic*`
- `Code` → `` `code` ``

You can also use HTML inside Markdown to apply color:

```html
<span style="color:green">This is green text</span>
```

---

### ✅ GUI or Web Projects

If you're using Python with a GUI framework or web app:

- **Tkinter**: Use font settings like `font=("Arial", 12, "bold")`.
- **HTML (for Flask/Django templates)**:
```html
<b>Bold</b>, <i>Italic</i>, <span style="color:blue">Blue</span>
```

---

📝 These techniques help you highlight or emphasize outputs in your Python applications.
