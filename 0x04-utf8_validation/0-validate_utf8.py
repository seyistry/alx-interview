#!/usr/bin/python3
"""
Validate if list of int are all valid UTF-8
"""


def validUTF8(data):
    for i in data:
        if i > 127:
            return False
    return True
