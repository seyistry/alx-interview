#!/usr/bin/python3
"""
pascal_triangle interview
"""
from math import factorial


def pascal_triangle(n):
    """pascal_triangle

    Args:
            n (int): size of triangle

    Returns:
            list: list of list
    """
    outer_list = []
    if n <= 0:
        return outer_list
    for i in range(n + 1):
        inner_list = []
        for j in range(i + 1):
            inner_list.append(
                int(factorial(i)/(factorial(j) * factorial(i - j))))
        outer_list.append(inner_list)
    return outer_list
