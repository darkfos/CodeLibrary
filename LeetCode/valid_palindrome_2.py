"""
    You are given an integer array nums consisting of n elements, and an integer k.

    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
    Any answer with a calculation error less than 10-5 will be accepted.
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #Easy

        if len(nums) < k:
            return sum(nums) / len(nums)

        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        for i in range(k, len(nums)):
            curr_sum = curr_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, curr_sum)

        return max_sum / k