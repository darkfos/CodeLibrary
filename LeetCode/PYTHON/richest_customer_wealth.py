"""
    You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

    A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
"""

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Easy
        return max([sum(x) for x in accounts])