#!/usr/bin/python3
"""a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """determines all boxes that can be opened"""
    if (type(boxes) is not list):
        return False

    if (len(boxes) == 0):
        return False

    the_keys = [0]
    for k in the_keys:
        for b in boxes[k]:
            if b not in the_keys and b != k and b < len(boxes) and b != 0:
                the_keys.append(b)
    if len(the_keys) == len(boxes):
        return True
    else:
        return False
