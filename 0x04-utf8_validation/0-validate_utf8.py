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
            d = bool(i & (1 << (7 - 1)))
            e = bool(i & (1 << (14 - 1)))
            check_onces = (a and b and c)
            check_zeroes = not (d or e)
            if not(check_onces and check_zeroes):
                return False
        elif i in range(65536, 16777216):
            a = bool(i & (1 << (8 - 1)))
            b = bool(i & (1 << (16 - 1)))
            c = bool(i & (1 << (22 - 1)))
            d = bool(i & (1 << (23 - 1)))
            e = bool(i & (1 << (24 - 1)))
            f = bool(i & (1 << (7 - 1)))
            g = bool(i & (1 << (15 - 1)))
            h = bool(i & (1 << (21 - 1)))
            check_onces = (a and b and c and d and e)
            check_zeroes = not (f or g or h)
            if not(check_onces and check_zeroes):
                return False
        elif i in range(16777216, 4294967296):
            a = bool(i & (1 << (8 - 1)))
            b = bool(i & (1 << (16 - 1)))
            c = bool(i & (1 << (24 - 1)))
            d = bool(i & (1 << (29 - 1)))
            e = bool(i & (1 << (30 - 1)))
            f = bool(i & (1 << (31 - 1)))
            g = bool(i & (1 << (32 - 1)))
            h = bool(i & (1 << (7 - 1)))
            j = bool(i & (1 << (15 - 1)))
            k = bool(i & (1 << (23 - 1)))
            l = bool(i & (1 << (28 - 1)))
            check_onces = (a and b and c and d and e and f and g)
            check_zeroes = not (j or j or k or l)
            if not(check_onces and check_zeroes):
                return False
        else:
            return False

    return True
