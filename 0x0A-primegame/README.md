# 0x0A. Prime Game

## Overview
Maria and Ben are playing a game where they take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n. The chosen number and its multiples are then removed from the set. The player who cannot make a move loses the game. They play multiple rounds of the game, each with a different value of n. The task is to determine, given the number of rounds and the values of n for each round, who wins each game assuming both players play optimally.

## Prototype
```python
def isWinner(x, nums):
    pass
```

### Parameters
- `x`: The number of rounds.
- `nums`: An array of integers representing the values of n for each round.

### Return
- The name of the player who won the most rounds.
- If the winner cannot be determined, return `None`.

## Constraints
- The values of n and x will not be larger than 10000.
- You cannot import any packages in this task.

## Example
```python
x = 3
nums = [4, 5, 1]

# First round: 4
# Maria picks 2 and removes 2, 4, leaving 1, 3
# Ben picks 3 and removes 3, leaving 1
# Ben wins because there are no prime numbers left for Maria to choose

# Second round: 5
# Maria picks 2 and removes 2, 4, leaving 1, 3, 5
# Ben picks 3 and removes 3, leaving 1, 5
# Maria picks 5 and removes 5, leaving 1
# Maria wins because there are no prime numbers left for Ben to choose

# Third round: 1
# Ben wins because there are no prime numbers for Maria to choose

# Result: Maria won 1 round, Ben won 2 rounds
# Therefore, Ben is the winner of the most rounds
```

## Implementation Guidelines
- Implement a function to determine if a number is prime.
- Consider implementing a function to generate prime numbers up to a given limit efficiently.
- Use dynamic programming or memoization techniques to optimize performance, especially for larger values of n.
