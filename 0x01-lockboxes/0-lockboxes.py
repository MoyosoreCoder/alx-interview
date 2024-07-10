#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    
    Args:
        boxes (list): List of lists containing keys for each box.
        
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    visited = set()
    stack = [0]
    
    while stack:
        current_box = stack.pop()
        if current_box not in visited:
            visited.add(current_box)
            for key in boxes[current_box]:
                if key < len(boxes):
                    stack.append(key)
                    
    return len(visited) == len(boxes)
