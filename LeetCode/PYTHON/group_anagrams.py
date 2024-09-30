"""
    Given an array of strings strs, group the
    anagrams
    together. You can return the answer in any order.
"""


from typing import List
class Solution:
    # Medium
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: dict = {}

        for string in strs:
            string_sort = "".join(sorted(string))
            if string_sort in anagrams:
                anagrams[string_sort].append(string)
            else:
                anagrams[string_sort] = [string]
        return list(anagrams.values())