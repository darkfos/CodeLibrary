from itertools import permutations as per

"""
    In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

    Create as many "shufflings" as you can!
"""


def permutations(s):
    # 4 kyu

    result = set(["".join(res) for res in per(s, len(s))])
    return list(result)