#!/usr/bin/python3
"""A function which uses two operations Copy All and Paste"""


def minOperations(n):
    """A function that show how the operations work"""
    if n <= 1:
        return 0

    # prime factors
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
        if n == 1:
            break

    # Calculates minimum ops
    ops = 0
    for factor in factors:
        if factor != 1:
            ops += factor
    return ops
