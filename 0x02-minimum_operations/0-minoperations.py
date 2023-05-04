#!/usr/bin/python3
"""Minimum Operations 

    Returns:
        int: return min operation of copy and paste
    """

# This prime factor is from GeekofGeek
# and contributed by Taranpreet.


def primeFactors(n):
    """calculate prime factors

    Args:
        n (int): int

    Returns:
        list: return a factors of int
    """
    arr = []
    c = 2
    while (n > 1):
        if (n % c == 0):
            arr.append(c)
            n = n / c
        else:
            c = c + 1
    return arr


def minOperations(n):
    """ method that calculates
        the fewest number of operations 
        needed to result in exactly n H 
        characters in the file.

    Args:
        n (int): minimum operation

    Returns:
        int: return an integer
    """
    sum = 0
    for i in primeFactors(n):
        sum = sum + i
    return sum
