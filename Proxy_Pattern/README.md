# Proxy Design Pattern - Python Example

This project demonstrates the **Proxy Design Pattern** using a secure document access scenario in Python. The proxy controls access to a sensitive document based on user roles.

---

## 📌 Concept

The **Proxy Pattern** provides a surrogate or placeholder for another object to control access to it. It's useful in cases like:

- Access control
- Lazy loading
- Logging
- Caching

---

## 📁 Project Structure

```
Proxy_Pattern/
├── document_interface.py        # Abstract interface for the document
├── secure_document.py           # Real subject - the actual secure document
├── document_proxy.py            # Proxy - controls access based on user role
└── main.py                      # Test the proxy behavior
```

---

## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have Python 3.6+ installed.
3. Run the main file using the command below:

```bash
python main.py
```

## 🧩 How It Works

- `Document`: An abstract base class that defines a common interface (`display`) for all document types.
- `SecureDocument`: The real subject that contains the actual document content.
- `DocumentProxy`: Controls access to `SecureDocument`. Only users with the `"admin"` role can view the document.
- `main.py`: Demonstrates both an admin and a guest trying to access the document.

---

## 🚀 Example Output

```
Admin trying to view document:
Loading secure document 'classified.txt' from disk...
Displaying document: classified.txt

Guest trying to view document:
Access Denied: You do not have permission to view this document.
```

---

## ✅ Benefits

- **Security**: Sensitive content is protected through role-based access.
- **Performance**: The real object is only created when access is granted.
- **Encapsulation**: Logic for access control is cleanly separated from the real object.

---

## 📚 Inspired By

This project is part of a series of pattern implementations based on the _"Design Patterns in Python"_ book.

---
