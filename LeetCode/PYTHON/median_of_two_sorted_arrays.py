from typing import List

from tomlkit import array


class Solution:
    """
        Hard.

        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
        The overall run time complexity should be O(log (m+n)).
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        new_list: list[int] = sorted(nums1+nums2)
        medium = len(new_list) // 2

        result: float = 0
        cnt: int = 0 #Check before return

        left: list[int] = [number for number in new_list[:medium-1]] #get left part
        right: list[int] = [number for number in new_list[medium:]] #get right part

        while len(left) != len(right):

            result += new_list[medium]
            cnt += 1

            del new_list[medium]

            medium = len(new_list) // 2

            #New part's
            right = [number for number in new_list[medium:]]
            left = [number for number in new_list[:medium]]

        return result / 2 if cnt > 1 else float(result)