from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Medium

        Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
        We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
        You must solve this problem without using the library's sort function.
        """

        for el1 in range(len(nums)):
            for el2 in range(el1+1, len(nums)):
                if nums[el1] > nums[el2]:
                    md = nums[el1]
                    nums[el1] = nums[el2]
                    nums[el2] = md
        return nums