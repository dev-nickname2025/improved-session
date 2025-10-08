# Bank Management System - Day 15 OOP Project

## Overview
This project demonstrates advanced Python OOP concepts using a **Bank Management System**.

## Features
- **Abstract Classes**: `Account` enforces deposit & withdraw methods
- **Inheritance**: `SavingsAccount` & `CurrentAccount` inherit `Account`
- **Multiple Inheritance**: `EmployeeAccount` inherits `SavingsAccount`, `Admin`, and `AuditLog`
- **Encapsulation**: Private balance variable with getter/setter
- **Polymorphism**: deposit and withdraw methods behave differently across account types
- **Super() & MRO**: Proper method resolution in multiple inheritance

## How to Run
1. Clone this repository
2. Run `python main.py`
3. Observe outputs for different accounts and employee operations