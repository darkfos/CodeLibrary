"""
    Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

    The distance between two indices i and j is abs(i - j), where abs is the absolute value function.  
"""

from typing import List

class Solution:
    # Easy
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexs = []

        for i in range(len(s)):
            cnt_min: int = len(s)
            for j in range(len(s)):
                if s[j] == c:
                    if abs(i-j) <= cnt_min:
                        cnt_min = abs(i - j)
            indexs.append(cnt_min)
        
        return indexs