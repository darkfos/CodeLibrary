"""
    The Tribonacci sequence Tn is defined as follows:
    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
    Given n, return the value of Tn.
"""


class Solution:
    # Easy
    def tribonacci(self, n: int, result: list = []) -> int:
        trib = self.generate_tribonacci(n)
        return trib[n]

    def generate_tribonacci(self, n, result: list = [0, 1, 1]) -> list:
        if n == 0:
            return result
        result.append(result[-1] + result[-2] + result[-3])
        return self.generate_tribonacci(n - 1)