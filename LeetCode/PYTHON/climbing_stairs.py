"""
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways
    can you climb to the top?
"""

class Solution:
    # Easy
    def climbStairs(self, n: int) -> int:
        prev_number_1: int = 0
        prev_number_2: int = 1

        for x in range(1, n+1):
            local: int = prev_number_1 + prev_number_2
            prev_number_1 = prev_number_2
            prev_number_2 = local
        return prev_number_2