# 💬 Chat Room – Mediator Design Pattern in Python

This project demonstrates the **Mediator Design Pattern** through a simple group chat system. Instead of users communicating directly with each other, a central mediator (chat room) manages message delivery, making the system more modular and easier to manage.

## 🧠 Design Pattern Overview

The **Mediator Pattern** defines an object that encapsulates how a set of objects interact. It promotes **loose coupling** by preventing objects from referring to each other directly, and it allows their interaction to be varied independently.

## 💡 Use Case: Group Chat Application

Imagine a group chat where multiple users send and receive messages. Instead of each user tracking all others, a central `ChatRoom` mediator handles message routing.

## 🧱 Components

- **Mediator Interface**: `ChatRoomMediator`  
  - Declares method(s) like `send_message(sender, message)`.

- **Concrete Mediator**: `ChatRoom`  
  - Manages registered users.
  - Forwards messages from a sender to all other users.

- **Colleague Class**: `User`  
  - Has methods:
    - `send(message)` – sends message via mediator.
    - `receive(sender, message)` – receives messages from the chat room.

## 🚀 How to Run

1. Ensure Python 3.6+ is installed.
2. Run the main script:

```bash
python main.py
```