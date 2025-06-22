# 💳 Payment System – Strategy Design Pattern in Python

This project demonstrates the **Strategy Design Pattern** through a simple online payment system. The pattern allows the payment method to be selected and swapped at runtime without modifying the core logic.

## 🧠 Design Pattern Overview

The **Strategy Pattern** defines a family of algorithms (in this case, payment methods), encapsulates each one, and makes them interchangeable. This allows the algorithm to vary independently from clients that use it.

## 📦 Use Case

An online store allows users to pay with different payment options:
- 💳 Credit Card
- 🅿️ PayPal
- 🪙 Cryptocurrency

Instead of hardcoding payment logic, we define separate strategy classes for each method and let the user choose the strategy dynamically.

## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have Python 3.6+ installed.
3. Run the main file using the command below:

```bash
python main.py
```


## 🧱 Components

- **Strategy Interface**: `PaymentStrategy`
  - Declares a `pay(amount)` method.
  
- **Concrete Strategies**:
  - `CreditCardPayment`
  - `PayPalPayment`
  - `CryptoPayment`
  
- **Context**: `PaymentProcessor`
  - Accepts a payment strategy and delegates the `pay()` operation to it.

## 🧰 Example Flow

1. User selects a payment method.
2. `PaymentProcessor` is initialized with the selected strategy.
3. Calling `processor.pay(100)` delegates the payment to the strategy.

## ✅ Benefits

- Follows the Open/Closed Principle — new payment methods can be added without modifying existing code.
- Payment algorithms are encapsulated and reusable.
- Strategies are interchangeable at runtime.

## 🛠️ Requirements

- Python 3.6 or higher
- No external libraries required

## 📚 Concepts Practiced

- Strategy Design Pattern
- Interfaces and Abstract Base Classes
- Object-Oriented Design Principles (Encapsulation, Polymorphism)

## 📌 Example Use Cases of Strategy Pattern

- Payment systems (like this)
- Sorting algorithms
- Compression strategies (ZIP, RAR, etc.)
- Route-finding in maps
- AI behavior in games


This project is great for understanding dynamic behavior swapping in a clean and maintainable way. Try adding new strategies like Apple Pay or Bank Transfer!
