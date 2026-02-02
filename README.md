# Session5-6HW

CLI program to calculate net income after tax based on gross income and number of children.

## Requirements
- Python 3.x

## How it works
- Prompts for `gross` (float) and `children` (int).
- Chooses a base tax rate by gross income:
  - `< 1000` → 10%
  - `< 2000` → 12%
  - `< 4000` → 14%
  - `>= 4000` → 18%
- Applies a child tax reduction:
  - Gross `< 2000` → `1%` per child
  - Gross `>= 2000` → `0.5%` per child
- Tax rate is floored at `0%`.
- Net = `gross - (gross * tax)`.

## Code
```bash
python3 Session5-6HW.py
Example
gross: 1500
children: 2
net: 1335.0
Notes
•
If non-numeric input is entered, the program prints: please enter digits only.
