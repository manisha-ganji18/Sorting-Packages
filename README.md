# Sorting-Packages
Coding Challenge to sort packages

# 📦 Thoughtful Sorting Challenge – Solution

Hi there! 👋  
This repository contains my Python solution for the **Thoughtful** robotic automation challenge.  
The goal was to write a function that determines which stack a package should go to based on its **volume** and **mass**.

---

## 🎯 Objective

Thoughtful’s robotic automation factory.  
Each package must be dispatched to the correct stack:

- **STANDARD** → Normal packages (not bulky or heavy)
- **SPECIAL** → Either bulky or heavy (but not both)
- **REJECTED** → Both bulky and heavy

The robotic arm uses this logic to sort packages automatically.

---

## 📐 Classification Rules

A package is:
- 🧱 **Bulky** if  
  - Volume (`width × height × length`) **≥ 1,000,000 cm³**, **or**  
  - Any dimension (width, height, length) **≥ 150 cm**
- ⚖️ **Heavy** if  
  - Mass **≥ 20 kg**

---

## 🧠 Logic

| Bulky | Heavy | Stack     |
|:-----:|:-----:|:----------|
| No    | No    | STANDARD  |
| Yes   | No    | SPECIAL   |
| No    | Yes   | SPECIAL   |
| Yes   | Yes   | REJECTED  |

---

## 💻 Function Definition

```python
def sort(width, height, length, mass) -> str:
    """
    Determines the correct stack based on package size and weight.
    Returns one of: "STANDARD", "SPECIAL", or "REJECTED"
    """
