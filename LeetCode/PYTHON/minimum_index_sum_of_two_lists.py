from typing import List

"""
    Given two arrays of strings list1 and list2, find the common strings
    with the least index sum.

    A common string is a string that appeared in both list1 and list2.
    A common string with the least index sum is a common string such
    that if it appeared at list1[i] and list2[j] then i + j should be the
    minimum value among all the other common strings.

    Return all the common strings with the least index sum. Return the answer in any order.
"""

class Solution:
    # Easy
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result: list = []
        
        for el1, el2 in zip(list1, list2):
            if el1 in list2 and el1 not in result:
                result.append((list1.index(el1)+list2.index(el1), el1))
            elif el2 in list1 and el2 not in result:
                result.append((list2.index(el2)+list1.index(el2), el2))
        min_indx = min(result, key=lambda x: x[0])[0]
        return list(set(el[-1] for el in result if el[0] <= min_indx))