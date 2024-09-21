from typing import List
"""
    Given an array of strings words, return the words that can be typed using letters of the alphabet on only one
    row of American keyboard like the image below.

    In the American keyboard:

    the first row consists of the characters "qwertyuiop",
    the second row consists of the characters "asdfghjkl", and
    the third row consists of the characters "zxcvbnm".
"""


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        #Easy

        line1 = ("q", "w", "e", "r", "t", "y", "u", "i", "o", "p")
        line2 = ("a", "s", "d", "f", "g", "h", "j", "k", "l")
        line3 = ("z", "x", "c", "v", "b", "n", "m")
        res: List[str] = []

        for word in words:
            local_set: set = set(map(lambda ch: 1 if ch.lower() in line1 else 2 if ch.lower() in line2 else 3,
             word))
            if len(local_set) == 1:
                res.append(word)
        return res