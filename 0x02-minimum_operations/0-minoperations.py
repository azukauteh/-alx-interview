#!/usr/bin/python3
"""Defines Minimum Operations """


def minOperations(n):
    if n <= 1:
        return 0

    """ Initialize array to store the minimum operations for each position"""
    dp = [float('inf')] * (n + 1)

    """ Base case: It takes 0 operations to have 1 'H' in the file """
    dp[1] = 0

    """ Iterate from 2 to n """
    for i in range(2, n + 1):
        """ Iterate from 1 to i - 1 to find a divisor"""
        for j in range(1, i):
            if i % j == 0:
                """ If j is a divisor of i, update dp[i] with the minimum
                    current value and dp[j] + (i/j)
                    """
                dp[i] = min(dp[i], dp[j] + (i // j))

    return dp[n] if dp[n] != float('inf') else 0
