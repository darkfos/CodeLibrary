from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Easy
        return sum(map(lambda x: 1 if all([el in allowed for el in x]) else 0, words))