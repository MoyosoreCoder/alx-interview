#!/usr/bin/python3
"""Module that exhibit copy and paste"""
def minOperations(n):
    """method that accept a single parameter and calculates the the fewest number
    of operations needed to result in exactly n H characters in the file."""

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
