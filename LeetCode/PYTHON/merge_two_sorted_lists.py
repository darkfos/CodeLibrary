from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.

    Easy
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        unpuck_lists: list[int] = self.unpuck_lists(lst1=list1, lst2=list2)
        return self.create_new_list_node(lst=unpuck_lists)

    def unpuck_lists(self, lst1: ListNode, lst2: ListNode) -> list[int]:
        cp_lst1: ListNode = lst1
        cp_lst2: ListNode = lst2

        result_lst: list[int] = []

        while cp_lst1 or cp_lst2:
            if cp_lst1:
                result_lst.append(cp_lst1.val)
                cp_lst1 = cp_lst1.next
            if cp_lst2:
                result_lst.append(cp_lst2.val)
                cp_lst2 = cp_lst2.next

        result_lst = self.quick_sort(result_lst)

        return result_lst

    def quick_sort(self, uns_lst: list[int]) -> list[int]:

        if len(uns_lst) <= 1:
            return uns_lst

        left_arr: list[int] = [el for el in uns_lst if el < uns_lst[len(uns_lst) // 2]]
        right_arr: list[int] = [el for el in uns_lst if el > uns_lst[len(uns_lst) // 2]]

        return self.quick_sort(left_arr) + [uns_lst[len(uns_lst) // 2]] * uns_lst.count(
            uns_lst[len(uns_lst) // 2]) + self.quick_sort(right_arr)

    def create_new_list_node(self, lst: list[int]) -> ListNode:

        if len(lst) <= 0:
            return None

        result_list_node: ListNode = ListNode(lst.pop(0))
        cp_result_list_node = result_list_node

        while lst:
            cp_result_list_node.next = ListNode(lst.pop(0))
            cp_result_list_node = cp_result_list_node.next

        return result_list_node