#!/usr/bin/python3
"""
pascal_triangle interview
"""
# from math import factorial


def factorial(n):
    """generate factorial

    Args:
        n (int): number of factorial

    Returns:
        int: return an int
    """
    if (n == 1 or n == 0):
        return 1
    else:
        return (n * factorial(n - 1))


def pascal_triangle(n):
    """pascal_triangle

    Args:
            n (int): size of triangle

    Returns:
            list: list of list
    """
    outer_list = []
    if n <= 0:
        return [[]]
    for i in range(n):
        inner_list = []
        for j in range(i + 1):
            inner_list.append(
                int(factorial(i)/(factorial(j) * factorial(i - j))))
        outer_list.append(inner_list)
    return outer_list
