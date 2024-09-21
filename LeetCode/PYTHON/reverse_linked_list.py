from typing import Optional


"""
    Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        elements_from_ln: list[int] = list()

        while head:
            elements_from_ln.append(head.val)
            head = head.next

        elements_from_ln = list(reversed(elements_from_ln))
        if elements_from_ln:
            new_ln: ListNode = ListNode(val=elements_from_ln[0])
            current_new_ln = new_ln
            for element in elements_from_ln[1:]:
                current_new_ln.next = ListNode(element)
                current_new_ln = current_new_ln.next
            return new_ln
        return None