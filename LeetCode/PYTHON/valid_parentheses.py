"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    # Easy
    def isValid(self, s: str) -> bool:
        stack: list = []
        dct: dict = {
            "(": ")", "{": "}", "[": "]"
        }

        for el in s:
            if el in dct.keys():
                stack.append(el)
            elif el in dct.values():
                if not stack or dct[stack[-1]] != el:
                    return False
                stack.pop()
        
        return not stack