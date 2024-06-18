from typing import List

"""
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Easy
        arr1, arr2 = nums[0:n], nums[n:]

        new_array: list = list()
        for els in zip(arr1, arr2):
            new_array.append(els[0])
            new_array.append(els[-1])

        return new_array