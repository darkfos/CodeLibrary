class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        result: int = 0
        result_str: str = ""
        while num2 or num1 or result:
            if num1:
                result += int(num1.pop())
            if num2:
                result += int(num2.pop())
            result_str += str(result % 10)
            result //= 10
        return result_str[::-1]