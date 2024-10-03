from itertools import permutations
from typing import List

"""
    Given a collection of numbers, nums, that might contain
    duplicates, return all possible unique permutations in any order.
"""

class Solution:
    # Medium
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result: list = []
        for lst in permutations(nums, len(nums)):
            if list(lst) not in result:
                result.append(list(lst))
        return result