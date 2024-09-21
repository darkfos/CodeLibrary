"""
    Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
    Given a balanced string s, split it into some number of substrings such that:

    Each substring is balanced.
    Return the maximum number of balanced strings you can obtain.

    Split a String in Balanced Strings
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        #Easy

        result: list = []
        local_str: str = ""
        for ch in s:
            local_str += ch
            if local_str.count("R") == local_str.count("L") and len(local_str) != 0:
                result.append(local_str)
                local_str = ""
        return len(result)