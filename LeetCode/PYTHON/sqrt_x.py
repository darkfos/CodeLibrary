"""
    Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
    The returned integer should be non-negative as well.

    You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        #Easy

        last_number: int = 0
        if x == 0: return 0
        for i in range(1, x+1):
            if (i*i) < x:
                last_number = i
            elif (i*i) > x:
                return last_number
            else:
                return i
