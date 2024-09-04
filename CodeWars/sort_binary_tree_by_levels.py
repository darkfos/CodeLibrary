"""
    Your task is to return the list with elements from tree sorted by levels, which
    means the root element goes first, then root children (from left to right) are
    second and third, and so on.

    Return empty list if root is None.
"""

class Node:

    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

def tree_by_levels(node, lst: list = []):
    #4 kyu
    
    if not node:
        return []
    else:

        nodes: list[Node] = [node]
        numbers: list[int] = []

        while nodes:
            new_node = nodes.pop(0)
            numbers.append(new_node.value)

            if new_node.left:
                nodes.append(new_node.left)
            if new_node.right:
                nodes.append(new_node.right)
    
        return numbers        