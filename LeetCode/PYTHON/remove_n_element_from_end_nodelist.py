from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    Medium
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        elements_from_list_node: list[int] = self.get_elements(head=head)[::-1]
        del elements_from_list_node[n-1]
        return self.create_new_list_node(lst_el=elements_from_list_node)

    def create_new_list_node(self, lst_el: list[int]) -> ListNode:

        if len(lst_el) <= 0:
            return None

        new_list_node = ListNode(lst_el.pop())
        cp_new_list_node = new_list_node

        while lst_el:
            cp_new_list_node.next = ListNode(lst_el.pop())
            cp_new_list_node = cp_new_list_node.next

        return new_list_node

    def get_elements(self, head: Optional[ListNode]) -> list[int]:
        new_head = head
        lst_nodes_elements: list[int] = []
        while new_head:
            lst_nodes_elements.append(new_head.val)
            new_head = new_head.next
        return lst_nodes_elements