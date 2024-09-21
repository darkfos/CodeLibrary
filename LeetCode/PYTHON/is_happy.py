"""
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in
    a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        #Easy

        if n < 10 and n % 2 == 0:
            return False
        cnt2: int = 9
        while n not in (0, 1):
            if cnt2 > 80:
                return False
            cnt = 0
            for numb in str(n):
                cnt += int(numb)**2
            n = cnt
            cnt2 += 1
        return n == 1