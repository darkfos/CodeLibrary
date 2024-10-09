"""
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci
    sequence, such that each number is the sum of the two preceding ones, starting from
    0 and 1. That is,
"""


class Solution:
    # Easy
    def fib(self, n: int) -> int:
        fib_numbers: list[int] = []
        if not n: return 0

        while n:
            if len(fib_numbers) >= 2:
                fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
            elif len(fib_numbers) == 1:
                fib_numbers.append(1)
            else:
                fib_numbers.append((0))
            n -= 1

        return fib_numbers[-1] + fib_numbers[-2] if len(fib_numbers) >= 2 else 1