from typing import List

"""
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
    non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters
    include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Easy

        new_str: str = "".join([ch.lower() for ch in s if ch.isalpha() or ch.isdigit()])
        return new_str == "".join(reversed(new_str))