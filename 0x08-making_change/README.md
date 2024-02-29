# 0x08. Making Change

## Overview
The "Making Change" function is a Python script designed to determine the minimum number of coins needed to meet a given total amount using a specified set of coin denominations. This function takes two inputs: a list of coin denominations available and the total amount to be met. It returns the fewest number of coins required to meet the total amount, considering that an infinite number of each denomination of coin is available.

## Usage
1. Input : The function `makeChange` takes two parameters:
   - `coins`: A list of integers representing the denominations of coins available. Each denomination should be an integer greater than 0.
   - `total`: An integer representing the total amount to be met using the available coins.

2. Output : The function returns an integer representing the minimum number of coins needed to meet the total amount. If the total is 0 or less, it returns 0. If the total cannot be met by any combination of the available coins, it returns -1.

3. Execution: To use the function, import it into your Python script or interactive session and call it with the appropriate arguments. For example:
    ```python
    from making_change import makeChange

    coins = [1, 2, 25]
    total = 37
    print(makeChange(coins, total))  # Output: 7

    coins = [1256, 54, 48, 16, 102]
    total = 1453
    print(makeChange(coins, total))  # Output: 8
    ```

## Example
```python
from making_change import makeChange

coins = [1, 2, 25]
total = 37
print(makeChange(coins, total))  # Output: 7

coins = [1256, 54, 48, 16, 102]
total = 1453
print(makeChange(coins, total))  # Output: 8
```

## Implementation Details
- The function uses a greedy approach to find the minimum number of coins needed to meet the total amount.
- It first sorts the list of coin denominations in descending order to consider larger denominations first.
- It iterates through the sorted list of denominations and adds coins to the total until the total amount is met or exceeded.
- If the total amount is met, the function returns the count of coins used. Otherwise, it returns -1 indicating that the total cannot be met using the available coins.

## Files
- `making_change.py`: Python script containing the implementation of the `makeChange` function.
- `README.md`: This README file providing an overview of the function, usage instructions, and implementation details.

