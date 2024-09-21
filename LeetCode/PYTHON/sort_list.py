from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #Medium

    """
        Given the head of a linked list, return the list after sorting it in ascending order.
    """


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        elements: list = self.get_elements(head=head)
        sorted_elements: list = self.get_sorted_elements(lst=elements)

        if not sorted_elements: return None

        new_listnode = ListNode(sorted_elements[0])
        cp_new_listnode = new_listnode

        for val in sorted_elements[1:]:
            cp_new_listnode.next = ListNode(val)
            cp_new_listnode = cp_new_listnode.next

        return new_listnode

    def get_sorted_elements(self, lst: list) -> list:

        if len(lst) < 2:
            return lst

        middle = lst[len(lst) // 2]
        left: list = [el for el in lst if el < middle]
        right: list = [el for el in lst if el > middle]

        return self.get_sorted_elements(left) + [middle] * lst.count(middle) + self.get_sorted_elements(right)

    def get_elements(self, head: ListNode):
        result: list = []

        while head:
            result.append(head.val)
            head = head.next

        return result
