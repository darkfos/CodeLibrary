from typing import Optional

"""
    Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
    Return the linked list sorted as well.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Easy

        unique_numbers: list[int] = []

        head_1 = head
        while head_1 and head_1.next:
            if head_1.val not in unique_numbers:
                unique_numbers.append(head_1.val)

            if head_1.next.val in unique_numbers:
                head_1.next = head_1.next.next
                continue
            head_1 = head_1.next
        return head