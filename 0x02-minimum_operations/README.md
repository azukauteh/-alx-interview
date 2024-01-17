

```markdown
# 0x02. Minimum Operations

## Introduction

This project aims to solve a problem related to file manipulation using two operations: Copy All and Paste. The goal is to find the minimum number of operations needed to achieve a specific number of characters ('H') in a file.

## Problem Description

Given a single character 'H' in a text file and the ability to perform Copy All and Paste operations, the task is to determine the fewest number of operations required to have exactly `n` 'H' characters in the file.

## Prototype

```python
def minOperations(n)
```

**Returns:**
- An integer representing the minimum number of operations.
- If it is impossible to achieve `n` 'H' characters, return 0.

## Example

```python
n = 9

# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

# Number of operations: 6
print(minOperations(n))
```

## Files

- `0-minoperations.py`: Python script containing the implementation of the `minOperations` function.
- `0-main.py`: Main file for testing the function with example cases.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/azukauteh/alx-interview.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x02-minimum-operations
   ```

3. Run the test script:

   ```bash
   ./ 0-main.py
   ```

```
