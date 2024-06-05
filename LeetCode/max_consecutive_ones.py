from typing import List
"""
    Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #Easy
        cnt: int = 0
        max_cnt: int = 0
        for number in nums:
            if number == 1:
                cnt += 1
                if cnt >= max_cnt: max_cnt = cnt
            else:
                cnt = 0

        return max_cnt