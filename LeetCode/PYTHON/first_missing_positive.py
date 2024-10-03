from typing import List
"""
    Given an unsorted integer array nums. Return the smallest
    positive integer that is not present in nums.
    You must implement an algorithm that runs in O(n) time
    and uses O(1) auxiliary space.
"""

class Solution:
    # Hard
    def firstMissingPositive(self, nums: List[int]) -> int:
        prev_num: int = 0
        nums = sorted(list(set([el for el in nums if el > 0])))
        if not nums:
            return 1
        if nums[0] == 1:
            for el in nums:
                if el == prev_num+1:
                    prev_num = el
                else:
                    return prev_num+1
            return prev_num+1
        else:
            return prev_num+1