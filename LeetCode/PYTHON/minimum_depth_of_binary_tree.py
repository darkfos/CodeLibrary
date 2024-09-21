from typing import Optional, List

"""
    Given a binary tree, find its minimum depth.
    
    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
    Note: A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #Easy
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        if root.left is None and root.right is not None:
            return 1 + self.minDepth(root.right)
        if root.left is not None and root.right is None:
            return 1+ self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))