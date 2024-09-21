"""
    Maximum Number of Ballons

    Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
    You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Easy

        b_word: int = text.count("b")
        a_word: int = text.count("a")
        l_word: int = text.count("l") // 2 if text.count("l") >= 2 else 0
        o_word: int = text.count("o") // 2 if text.count("o") >= 2 else 0
        n_word: int = text.count("n")

        return min((b_word, a_word, l_word, o_word, n_word))