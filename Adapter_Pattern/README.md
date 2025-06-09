# 🧩 Adapter Design Pattern – Payment Gateway Example

## 📌 Purpose

The Adapter Design Pattern allows incompatible interfaces to work together by acting as a bridge between them. It lets classes work together that couldn’t otherwise due to incompatible interfaces.

This project demonstrates the adapter pattern through a **payment gateway system** where an old third-party payment service is adapted to fit into a unified interface used across the application.

---

## 💡 Problem

We have a system that expects a standard interface for all payment gateways:

```python
class PaymentGateway:
    def pay(self, amount): ...
```

But there's a legacy payment service (e.g., `OldPaySystem`) which has a different interface:

```python
class OldPaySystem:
    def make_payment(self, money): ...
```

Changing the legacy code isn't ideal — instead, we apply the Adapter pattern.

---

## 🛠️ Solution

We create an adapter class `OldPayAdapter` that wraps `OldPaySystem` and translates calls to the expected interface:

```python
class OldPayAdapter(PaymentGateway):
    def __init__(self, old_payment):
        self.old_payment = old_payment

    def pay(self, amount):
        self.old_payment.make_payment(amount)
```

Now, our system can use `OldPaySystem` as if it was a native `PaymentGateway`.

---

## 🧪 Example Usage

```python
# Legacy payment system
old_gateway = OldPaySystem()

# Adapter makes it compatible
payment = OldPayAdapter(old_gateway)

# Unified interface usage
payment.pay(100)
```

---

## ✅ Benefits

- Promotes **code reusability** without modifying existing code.
- Makes integration of **legacy systems** smoother.
- Encourages a **clean interface design**.

