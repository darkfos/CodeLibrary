from typing import List

"""
    Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""


class Solution:
    # Medium
    def maxSubArray(self, nums: List[int]) -> int:
        mx = 0
        number: int = 0
        for n in range(len(nums)):
            number += nums[n]
            if number > mx:
                mx = number
            if number < 0:
                number = 0
        return mx if mx else max(nums)