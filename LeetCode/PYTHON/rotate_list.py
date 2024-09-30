from typing import Optional

"""
    Given the head of a linked list, rotate the list to the right by k places.
"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Medium

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next is None or k == 0: return head
        elements: list = self.get_elements(node=head)
        slices: int = k % len(elements)
        while slices:
            elements.insert(0, elements.pop(-1))
            slices -= 1
        return self.create_node(lst=elements)
    
    def get_elements(self, node: ListNode):
        els: list[int] = []

        while node:
            els.append(node.val)
            node = node.next
        
        return els

    def create_node(self, lst: list[int]) -> ListNode:
        new_node: ListNode = ListNode(lst.pop(0))
        new_node_cp = new_node

        while lst:
            new_node_cp.next = ListNode(lst.pop(0))
            new_node_cp = new_node_cp.next

        return new_node