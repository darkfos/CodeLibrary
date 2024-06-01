"""
    You are given a string s. The score of a string is defined as the sum of the absolute difference between
    the ASCII values of adjacent characters.

    Return the score of s.
"""


class Solution:
    def scoreOfString(self, s: str) -> int:
        #Easy

        res: int = 0
        count: int = 0
        while count != len(s)-1:
            res += abs(ord(s[count]) - ord(s[count+1]))
            count += 1
        return res