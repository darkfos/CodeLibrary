"""
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by deleting some
    (can be none) of the characters without disturbing the relative positions of the remaining characters.
    (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


class Solution:
    # Easy
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        finded: bool = False
        result: int = 0

        for el in s:
            for el2 in range(len(t)):
                if el == t[el2]:
                    t = t[el2+1:]
                    result += 1
                    finded = True
                    break
            if finded:
                finded = False
                continue
            else:
                return False
        return result == len(s)