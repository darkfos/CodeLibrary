from typing import List

"""
    Given an array of integers nums, return the number of good pairs.
    A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #Easy

        return sum((1 for j in range(len(nums)) for i in range(len(nums)) if nums[i] == nums[j] and i < j))