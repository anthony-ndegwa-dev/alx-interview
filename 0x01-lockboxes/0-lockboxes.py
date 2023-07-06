#!/usr/bin/python3
""" You've n number of locked boxes. Each box is numbered sequentially
from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
        There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    # Get total number of boxes
    total_boxes = len(boxes)
    # A list to keep trach of unlocked boxes, initially set to False
    unlocked_boxes = [False] * total_boxes
    # First box is always unlocked
    unlocked_boxes[0] = True
    # Start to check from first box
    keys_to_check = [0]

    while keys_to_check:
        # Get key from current box
        current_box = keys_to_check.pop()

        # Iterate over the keys in the current box
        for key in boxes[current_box]:
            if key < total_boxes and not unlocked_boxes[key]:
                # Unlock the box corresponding to the key
                unlocked_boxes[key] = True
                # Add the new key to the keys_to_check list
                keys_to_check.append(key)

    # Checks if all boxes are unlocked and return result
    return all(unlocked_boxes)
