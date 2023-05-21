#!/usr/bin/python3
"""
Validate if list of int are all valid UTF-8
"""


# def validUTF8(data):
#     for i in data:
#         x = bool(i & (1 << (8 - 1)))
#         if x is True:
#             return False
#     return True


def validUTF8(data):
    """
    :type data: List[int]
    :rtype: bool
    """
    count = 0
    for c in data:
        if count == 0:
            if (c >> 5) == 0b110:
                count = 1
            elif (c >> 4) == 0b1110:
                count = 2
            elif (c >> 3) == 0b11110:
                count = 3
            elif (c >> 7):
                return False
        else:
            if (c >> 6) != 0b10:
                return False
            count -= 1
    return count == 0
