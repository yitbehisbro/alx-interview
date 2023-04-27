#!/usr/bin/python3
""" A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """ Checks if all the boxes can be opened """
    if not boxes:
        return False
    size = len(boxes)
    checker = {}
    index = 0

    for box in boxes:
        if len(box) == 0 or index == 0:
            checker[index] = -1
        for key in box:
            if key < size and key != index:
                checker[key] = key
        if len(checker) == size:
            return True
        index += 1
    return False
