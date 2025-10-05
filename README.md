# Sorting-Packages
Coding Challenge to sort packages

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
