"""
    Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.

    Return as a number.
"""


def div_con(lst: list):
    #7 kyu
    return sum(list(map(lambda numb: int(numb)*-1 if isinstance(numb, str) else numb, lst)))