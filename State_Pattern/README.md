# 🥤 Vending Machine – State Design Pattern in Python

This project demonstrates the **State Design Pattern** by simulating the behavior of a vending machine that changes its behavior based on its current state. The machine supports inserting money, selecting items, dispensing, and canceling transactions.

## 🧠 Design Pattern Overview

The **State Pattern** allows an object to alter its behavior when its internal state changes. It eliminates complex conditional logic and distributes responsibility across state-specific classes.

## 💡 Use Case: Vending Machine

A vending machine behaves differently depending on its current state. This implementation includes the following states:

- 🔵 **IdleState**: Waiting for the user to insert money.
- 💰 **HasMoneyState**: User has inserted money, waiting for item selection.
- 📦 **DispensingState**: Machine is dispensing the selected item.

> Note: `OutOfStockState` is not implemented in this version.

## 🧱 Components

- **Context**: `VendingMachine` 
- **Abstract State Interface**: `VendingMachineState`
- **Concrete States**:
  - `IdleState`: Accepts money, rejects all other actions.
  - `HasMoneyState`: Accepts item selection or money ejection.
  - `DispensingState`: Dispenses item and returns to idle.

## 🚀 How to Run

1. Make sure Python 3.6+ is installed.
2. Run the main script:

```bash
python main.py
```