#!/usr/bin/python3
"""Checks the boxes to see if they have a key."""


def canUnlockAll(boxes):
    opened = set()
    not_open = set((0,))
    while len(not_open) > 0:
        k = not_open.pop()
        if k < len(boxes):
            opened.update((k,))
            not_open.update(set(boxes[k]).difference(opened))
    return len(opened) == len(boxes)
