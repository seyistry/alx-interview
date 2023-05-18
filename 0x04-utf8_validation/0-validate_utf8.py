#!/usr/bin/python3
"""
Validate if list of int are all valid UTF-8
"""


def validUTF8(data):
    for i in data:
        if i in range(1, 256):
            a = bool(i & (1 << (8 - 1)))
            if a is True:
                return False
        elif i in range(256, 65536):
            a = bool(i & (1 << (8 - 1)))
            b = bool(i & (1 << (15 - 1)))
            c = bool(i & (1 << (16 - 1)))
            if (a and b and c) is not True:
                return False
        elif i in range(65536, 16777216):
            a = bool(i & (1 << (8 - 1)))
            b = bool(i & (1 << (16 - 1)))
            c = bool(i & (1 << (22 - 1)))
            d = bool(i & (1 << (23 - 1)))
            e = bool(i & (1 << (24 - 1)))
            if (a and b and c and d and e) is not True:
                return False
        elif i in range(16777216, 4294967296):
            a = bool(i & (1 << (8 - 1)))
            b = bool(i & (1 << (16 - 1)))
            c = bool(i & (1 << (24 - 1)))
            d = bool(i & (1 << (29 - 1)))
            e = bool(i & (1 << (30 - 1)))
            f = bool(i & (1 << (31 - 1)))
            g = bool(i & (1 << (32 - 1)))
            if (a and b and c and d and e and f and g) is not True:
                return False
        else:
            return False

    return True
