#!/usr/bin/python3
'''Find out if the room has all the keys for the room returns a boolean.'''


def canUnlockAll(boxes):
  '''check if user and unlock all boxes'''
  visited = set()
  queue = set((0,))
  while len(queue) > 0:
    key = queue.pop()
    if key < len(boxes):
      visited.update((key,))
      queue.update(set(boxes[key]).difference(visited))
  return len(visited) == len(boxes)
