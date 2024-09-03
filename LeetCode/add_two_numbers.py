from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
        reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as
        a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """
    #Middle

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        listnode = ListNode()
        l1_last: bool = False
        l2_last: bool = False
        str_number_1: str = ""
        str_number_2: str = ""
        localnode = listnode

        while True:

            if l1_last and l2_last: break

            l1_numb, l2_numb = 0 if l1_last is True else l1.val, 0 if l2_last is True else l2.val

            str_number_1 += str(l1_numb)
            str_number_2 += str(l2_numb)

            if l1.next is None:
                l1_last = True
            if l2.next is None:
                l2_last = True

            l1, l2 = l1 if l1_last is True else l1.next, l2 if l2_last is True else l2.next

        str_number_1 = int(str_number_1[::-1])
        str_number_2 = int(str_number_2[::-1])

        numb_for_node: str = str(str_number_1 + str_number_2)[::-1]
        listnode.val = int(numb_for_node[0])

        for n in numb_for_node[1:]:
            localnode = self.add_new_node(localnode, n=int(n))

        return listnode

    def add_new_node(self, node: ListNode, n):
        node.next = ListNode(n)
        return node.next