from typing import List

"""
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
"""


class Solution:
    #Easy

    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref: list = []
        for word in strs:
            for word2 in strs:
                check = self.check_word(word=word, word2=word2)
                if check not in pref:
                    pref.append(check)
        if pref:
            return "".join(map(lambda s: "".join(s[0]), min(pref, key=len)))
        return "".join(strs)

    def check_word(self, word, word2) -> list:
        res: list = []
        for ch in zip(word2, word):
            if ch[0] == ch[-1]:
                res.append(ch)
            else:
                break
        return res