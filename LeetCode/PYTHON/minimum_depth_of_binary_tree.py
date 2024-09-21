from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: set = set()
        lst: list = [root]

        if root:
            while lst:
                node = lst.pop()
                if node.left:
                    lst.append(node.left)
                if node.right:
                    lst.append(node.right)
                result.add(node.val)
            return result
        else: return list({})

root = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(10)
print(
    Solution().inorderTraversal(
        root=root
    )
)