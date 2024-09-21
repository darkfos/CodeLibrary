"""
    You are given an integer array nums. In one operation, you can add or subtract 1 from
    any element of nums.

    Return the minimum number of operations to make all elements of nums divisible by 3.

    

    Example 1:

    Input: nums = [1,2,3,4]

    Output: 3

    Explanation:

    All array elements can be made divisible by 3 using 3 operations:

        Subtract 1 from 1.
        Add 1 to 2.
        Subtract 1 from 4.

    Example 2:

    Input: nums = [3,6,9]

    Output: 0
"""

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #Easy
        
        cnt_try: int = 0
        id_number: int = 0

        while id_number != len(nums):
            if nums[id_number] % 3 == 0:
                cnt_try -= 1
                id_number += 1
            else:
                if nums[id_number] % 3 == 1:
                    nums[id_number] -= 1
                else:
                    nums[id_number] += 1
            cnt_try += 1
        
        return cnt_try