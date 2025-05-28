# Package Sorting Program

This program sorts packages into three categories (STANDARD, SPECIAL, or REJECTED) based on their dimensions and mass.

## Requirements

- Python 3.x

## Usage

The program provides a `sort()` function that takes four parameters:
- `width`: width of the package in centimeters
- `height`: height of the package in centimeters
- `length`: length of the package in centimeters
- `mass`: mass of the package in kilograms

Example usage:

```python
from sort import sort

# Example package: 100cm x 100cm x 100cm, 15kg
result = sort(100, 100, 100, 15)
print(result)  # Output: SPECIAL
```

## Categories

- **STANDARD**: Package is neither bulky nor heavy
- **SPECIAL**: Package is either bulky or heavy
- **REJECTED**: Package is both bulky and heavy

A package is considered:
- Bulky if its volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm
- Heavy if its mass ≥ 20 kg 