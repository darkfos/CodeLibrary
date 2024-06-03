"""
    Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

    Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
    Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
"""


from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #Easy

        arr3: List[int] = []
        not_in_array: List[int] = []
        for el in arr2:
            for el2 in arr1:
                if el == el2:
                    arr3.append(el2)
                elif el2 not in arr2 and el2 not in not_in_array:
                    cnt_el2 = arr1.count(el2)
                    not_in_array.extend([el2]*cnt_el2)
        arr3.extend(sorted(not_in_array))
        return arr3