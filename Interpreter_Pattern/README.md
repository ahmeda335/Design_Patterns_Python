# 🧮 Arithmetic Expression Interpreter – Interpreter Design Pattern in Python

This project demonstrates the **Interpreter Design Pattern** by evaluating arithmetic expressions using a simple grammar. The interpreter processes expressions composed of numbers, additions, and subtractions, and returns the final result by building an abstract syntax tree (AST).

## 🧠 Design Pattern Overview

The **Interpreter Pattern** is used to define a grammar for a language and provide an interpreter to evaluate expressions written in that language. It's useful for building interpreters, parsers, expression evaluators, and domain-specific languages (DSLs).

## 💡 Use Case: Arithmetic Expression Evaluator

Given a string expression like:

"2 + 5 - 1 + 10"

The interpreter builds an abstract syntax tree (AST) to evaluate the result using class-based representations of numbers and operations.

## 🧱 Components

- **Terminal Expression**: `Number`  
  Represents a constant integer in the expression. Implements `interpret()` to return its value.

- **Non-Terminal Expressions**: `Add`, `Subtract`  
  Represent binary operations. They store left and right expressions and implement `interpret()` to compute the result recursively.

- **AST Construction**:  
  A simple parser splits the expression string into tokens and builds the AST manually.

## 📦 Project Structure

- `main.py`: Main script to evaluate the expression  
- `number.py`: Defines the `Number` class  
- `sign.py`: Defines `Add` and `Subtract` operation classes

## 🚀 How to Run

1. Ensure you have Python 3.6 or higher installed.  
2. Run the main script:

```bash
python main.py
```