#!/usr/bin/python3
'''Solve lockboxes problem'''


def canUnlockAll(boxes):
    '''Solve lockboxes problem'''
    unlocked = {0: True}
    for i, box in enumerate(boxes):
        for key in box:
            if key != i and key < len(boxes):
                unlocked[key] = True
    return len(unlocked) == len(boxes)
