from typing import Optional

"""
    Given a linked list, swap every two adjacent nodes and return its head. You must solve
    the problem without modifying the values in the list's nodes (i.e., only nodes themselves
    may be changed.)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Medium
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        header = head
        cnt: int = 0

        if not header: return head

        while header.next:
            local = header.val
            if cnt % 2 == 0:
                header.val = header.next.val
                header.next.val = local
            header = header.next
            cnt += 1
        return head
    