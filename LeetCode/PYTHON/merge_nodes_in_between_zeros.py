from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        Medium

        You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
        For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
        Return the head of the modified linked list.
    """

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        number: int = 0
        cnt_zero: int = 0

        new_node = ListNode(val=1)
        new_node_copy = new_node

        while head:
            if head.val == 0:
                cnt_zero += 1
                if cnt_zero == 2:
                    new_node_copy.next = ListNode(number)
                    new_node_copy = new_node_copy.next
                    cnt_zero = 1
                    number = 0
            else:
                number += head.val
            head = head.next

        return new_node.next