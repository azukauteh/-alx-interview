# 0x00. Pascal's Triangle

## Description

This project explores the concept of Pascal's Triangle and includes functions to generate and print Pascal's Triangle.

## Files

- 0-pascal_triangle.py : Python script containing a function to compute Pascal's Triangle up to a given number of rows.
- tests: Directory containing test cases for the function.

## Functionality

1. generate_pascal_triangle(rows):
   - Generates Pascal's Triangle up to the specified number of rows.
   - Returns a list of lists representing Pascal's Triangle.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/azukauteh/alx-interview.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x00-Pascals_Triangle
   ```


3. Run the test cases:

   ```bash
    ./0-main.py
   ```

## Example

Suppose you want to generate Pascal's Triangle with 5 rows. Using the function:

```python
from 0-pascal_triangle import generate_pascal_triangle

rows = 5
triangle = generate_pascal_triangle(rows)
print(triangle)
```

The output will be:

```python
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```

## Author

Your Name

## Acknowledgments

Special thanks to anyone who contributed or inspired this project.

## Project Status

This project is complete and serves as a simple introduction to Pascal's Triangle in Python. Feel free to use, modify, or expand upon it!
