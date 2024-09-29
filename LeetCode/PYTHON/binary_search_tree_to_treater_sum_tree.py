# Definition for a binary tree node.
"""
    Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

    As a reminder, a binary search tree is a tree that satisfies these constraints:

        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Medium
    def bstToGst(self, root: TreeNode) -> TreeNode:
        head = root
        all_numbers = self.get_numbers(head=head)
        lst_nodes: list = [head]

        while lst_nodes:
            node = lst_nodes.pop(-1)
            if node:
                node.val = sum([x for x in all_numbers if x >= node.val]) if node.val is not None else None
                if node.left:
                    lst_nodes.append(node.left)
                if node.right:
                    lst_nodes.append(node.right)

        return head

    def get_numbers(self, head: TreeNode) -> list:
        lst: list = []
        list_nodes: list = [head]

        while list_nodes:
            last = list_nodes.pop(-1)
            if last:
                if last.val is not None:
                    lst.append(last.val)
                if last.left:
                    list_nodes.append(last.left)
                if last.right:
                    list_nodes.append(last.right)
        return lst

head = TreeNode(0)
head.right = TreeNode(None)
head.right.right = TreeNode(1)

print(Solution().bstToGst(root=head))