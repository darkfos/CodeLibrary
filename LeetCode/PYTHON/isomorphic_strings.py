class Solution:
    """
    Easy

    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters
    in s can be replaced to get t.
    All occurrences of a character must be replaced
    with another character while preserving the order of
    characters. No two characters may map to the same character,
    but a character may map to itself.
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        history: dict = {}
        for ch1, ch2 in zip(s, t):
            if ch1 in history:
                if history[ch1] == ch2:
                    continue
                else:
                    return False
            else:
                if ch2 in history.values():
                    return False
                history[ch1] = ch2
        return True
