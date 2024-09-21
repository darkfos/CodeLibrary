"""
    Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Medium

        substrings_set: str = set()
        if s == "":
            return 0
        for ch1 in range(len(s)):
            local_string: str = ""
            for ch2 in range(ch1, len(s)):
                if s[ch2] not in local_string:
                    local_string += s[ch2]
                else:
                    break
            substrings_set.add(local_string)
        res = max(substrings_set, key=lambda x: len(x))

        return len(res)
