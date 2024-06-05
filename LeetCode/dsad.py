class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res: list = []
        for num1 in range(len(s)):
            local_str: str = ""
            for num2 in range(num1, len(s)):
                local_str += s[num2]
                if local_str.count("1") == local_str.count("0") and local_str != s:
                    if local_str[-2] == local_str[-1] or len(local_str) <= 2:
                        res.append(local_str)
        return len(res)

test = Solution().countBinarySubstrings("10101")
print(test)