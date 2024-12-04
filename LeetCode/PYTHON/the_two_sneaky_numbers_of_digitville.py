from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        """
        # Easy
        In the town of Digitville, there was a list of numbers called nums containing
        integers from 0 to n - 1. Each number was supposed to appear exactly once in the
        list, however, two mischievous numbers sneaked in an additional time, making the
        list longer than usual.
        As the town detective, your task is to find these two sneaky numbers. Return
        an array of size two containing the two numbers (in any order), so peace can
        return to Digitville.
        """

        new_nums: list[int] = []
        for number in nums:
            if number not in new_nums and nums.count(number) == 2:
                new_nums.append(number)
        return sorted(new_nums)