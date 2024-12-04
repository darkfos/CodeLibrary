from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Easy

    A binary tree's maximum depth is the number of nodes along the longest path
    from the root node down to the farthest leaf node.
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        """

        elements: list[TreeNode] = [root]
        cnt_level: int = 0

        if not elements[0]: return 0

        while elements:
            for _ in range(len(elements)):
                el = elements.pop(0)
                if el.left:
                    elements.append(el.left)
                if el.right:
                    elements.append(el.right)
            cnt_level += 1

        return cnt_level