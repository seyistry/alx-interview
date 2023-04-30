#!/usr/bin/python3
"""
Lockboxes interview
"""

# box 0 is always unlocked
# if box is unlocked keep all key in box
# move to next box
# check box if key exist or if index in box unlock
# move to next box


def find_indices(list_to_check, item_to_find):
    """Generate indexes

    Args:
        list_to_check (list): list to check
        item_to_find (bool): item to find

    Returns:
        list: list of indexes
    """
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices


def canUnlockAll(boxes):
    """check if all boxes can unlock

    Args:
            boxes (list): a list of list
    """

    ownedKeys = []
    unlock = [True]
    for key in range(len(boxes)):
        if key == 0:
            ownedKeys.extend(boxes[0])
        else:
            if key == len(boxes) - 2:
                locked = find_indices(unlock, False)
                for falseKeyIndex in locked:
                    if falseKeyIndex in ownedKeys:
                        ownedKeys.extend(boxes[falseKeyIndex])
                        unlock[falseKeyIndex] = True
            if (key in ownedKeys or key in boxes[key]):
                ownedKeys.extend(boxes[key])
                unlock.append(True)
            else:
                unlock.append(False)

    if False in unlock:
        return False
    else:
        return True
