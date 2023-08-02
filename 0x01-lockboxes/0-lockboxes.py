#!/usr/bin/python3
"""A module that determines if all the boxes can be opened."""


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
