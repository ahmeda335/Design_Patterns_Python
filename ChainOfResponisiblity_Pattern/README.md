# 🏦 ATM Dispenser - Chain of Responsibility Pattern

This project is an implementation of the **Chain of Responsibility** design pattern, demonstrated through a simple ATM dispenser. The ATM dispenses money in denominations of $200, $100, and $50.

---

## 🧠 Design Pattern Used

**Chain of Responsibility** is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

---

## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have Python 3.6+ installed.
3. Run the main file using the command below:

```bash
python main.py
```
---

## ⚙️ Components

### 🧩 Abstract Handler - `Dispenser`
Defines the interface for handling requests and setting the next handler in the chain.

### 🏦 Concrete Handlers
- `Dollar200Dispenser`: Handles dispensing $200 notes.
- `Dollar100Dispenser`: Handles dispensing $100 notes.
- `Dollar50Dispenser`: Handles dispensing $50 notes.

Each handler checks if it can process the amount, and passes the remainder to the next handler.

### 🔗 Chain Builder - `ATMDispenserChain`
Initializes and links the chain of handlers:
```
$200 → $100 → $50
```

---

## 🚀 Usage

```python
from dispenser_chain import ATMDispenserChain

atm = ATMDispenserChain()
amounts = [750, 150, 50]  # Must be multiples of 50

for amount in amounts:
    print(amount)
    atm.chain1.handle(amount)
    print('-' * 30)
```

### ✅ Output

```
750
Dispensing 3 $200 note
Dispensing 1 $100 note
Dispensing 1 $50 note
------------------------------
150
Dispensing 1 $100 note
Dispensing 1 $50 note
------------------------------
50
Dispensing 1 $50 note
------------------------------
```

---

## 📌 TODO

- [ ] Add validation for non-multiples of 50.
- [ ] Add support for custom denominations.
- [ ] Enhance with logging or GUI.

---

## 📚 Pattern Advantages

- Reduces coupling between sender and receiver.
- Simplifies object interactions.
- Makes the system more flexible and extensible.

---

## 📘 Based On

This implementation was built after learning from the _"Design Patterns in Python"_ book, applying practical understanding of the Chain of Responsibility pattern.
