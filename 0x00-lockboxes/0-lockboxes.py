#!/usr/bin python3
""" Find out if the room has all the keys for the room return a boolean."""

def canUnlockAll(boxes):
  """check if user and unlock all boxes"""
  queue = [0]
  visited = { 0 }
  while queue:
    rm = queue.pop() #visited room
    for key in boxes[rm]:
      if key in visited:
        continue #key is already added to the room
      visited.add(key)
      queue.append(key)
  return len(visited) == len(boxes)
