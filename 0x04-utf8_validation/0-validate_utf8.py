#!/usr/bin/python3
"""
Validate if list of int are all valid UTF-8
"""


def validUTF8(data):
    for i in data:
        x = bool(i & (1 << (8 - 1) ))
        if x == True:
            return False
    return True
    