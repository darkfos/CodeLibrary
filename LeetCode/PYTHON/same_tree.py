from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #Easy
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.get_elements(p) == self.get_elements(q)

    @classmethod
    def get_elements(cls, nodes: TreeNode):

        if not nodes: return []

        result: list = []
        lst_nodes: list = [nodes]

        while lst_nodes:
            node = lst_nodes.pop()
            result.append(node.val if node else None)
            if node.left:
                lst_nodes.append(node.left)
            if node.right:
                lst_nodes.append(node.right)
            else:
                result.append(None)
        return result
