"""
    Consider the number triangle below, in which each number is equal to the number above plus the number to the left. If there is no number above, assume it's a 0.

    1
    1 1
    1 2 2
    1 3 5 5
    1 4 9 14 14

    The triangle has 5 rows and the sum of the last row is sum([1,4,9,14,14]) = 42.

    You will be given an integer n and your task will be to return the sum of the last row of a triangle of n rows.

    In the example above:

    solve(5) = 42

    More examples in test cases. Good luck!
"""


def solve(n):
    #6 kyu

    triangle: list = []
    for i in range(1, n+1):
        if triangle:
            local_line: list = []
            for line in range(i):
                if local_line:
                    local_line.append((triangle[-1][line] if line <= len(triangle[-1])-1 else 0) + local_line[-1])
                else:
                    local_line.append(1)
            triangle.append(local_line)
        else:
            triangle.append([1])
    return sum(triangle[-1])