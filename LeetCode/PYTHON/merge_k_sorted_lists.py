from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        Hard

        You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
        Merge all the linked-lists into one sorted linked-list and return it.
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        all_lists: list[int] = []

        for lst in lists:
            all_lists.extend(self.find_all_el_in_list(lst))

        if not all_lists: return None

        return self.create_list_node(sorted(all_lists))

    def create_list_node(self, lst: list[int]) -> ListNode:
        new_list_node = ListNode()
        copy_list_node = new_list_node

        while lst:
            if len(lst) == 1:
                copy_list_node.val = lst.pop(0)
            else:
                copy_list_node.val = lst.pop(0)
                copy_list_node.next = ListNode()
                copy_list_node = copy_list_node.next
        return new_list_node

    def find_all_el_in_list(self, list: ListNode) -> list:
        head = list
        res: list = []

        while head:
            res.append(head.val)
            head = head.next
        return res