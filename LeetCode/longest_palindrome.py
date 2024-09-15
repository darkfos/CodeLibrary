class Solution:
    """
        Medium

        Given a string s, return the longest palindromic
    """

    def longestPalindrome(self, s: str) -> str:
        result_str: str = ""

        for s1 in range(len(s)):
            local_str: str = ""
            cnt = 0
            string = s[s1:]
            while cnt != len(string):
                local_str += string[cnt]
                if local_str == local_str[::-1]:
                    if len(local_str) > len(result_str):
                        result_str = local_str
                cnt += 1
        return result_str