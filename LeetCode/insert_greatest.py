from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
        Medium

        Given the head of a linked list head, in which each node contains an integer value.
        Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
        Return the linked list after insertion.
        The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
    """

    def insertGreatestCommonDivisors(self, header: Optional[ListNode]) -> Optional[ListNode]:
        if header.next is None: return header

        result_lst = self.get_all_elements_from_node(node=header)
        new_node = ListNode(result_lst.pop(0))
        copy_new_node = new_node
        
        while result_lst:
            copy_new_node.next = ListNode(result_lst.pop(0))
            copy_new_node = copy_new_node.next
        return new_node

        
    
    @staticmethod
    def find_max_divisors(number_1: int, number_2: int) -> int:
        mx = max(number_1, number_2)

        while mx > 0:
            if number_1 % mx == 0 and number_2 % mx == 0:
                return mx
            mx -= 1

    def get_all_elements_from_node(self, node: ListNode):
        result_lst: list = []
        cnt_flag: int = 1
        is_skip: int = 1

        while node:
            if cnt_flag % 2 == 0:
                result_lst.append(
                    self.find_max_divisors(node.val, result_lst[-1])
                )
                cnt_flag += 1
            elif cnt_flag % 2 != 0 and node.next is None:
                result_lst.append(
                    self.find_max_divisors(node.val, result_lst[-1])
                )
            result_lst.append(node.val)
            cnt_flag += 1
            node = node.next

        return result_lst

head = ListNode(18)
head.next = ListNode(6)
head.next.next = ListNode(10)
head.next.next.next = ListNode(3)

rs = Solution().insertGreatestCommonDivisors(header=head)
while rs:
    print(rs.val)
    rs = rs.next