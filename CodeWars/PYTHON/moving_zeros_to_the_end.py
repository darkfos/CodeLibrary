"""
    Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

    move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst):
    # 6 kyu

    not_zeros_numbers: list = list(filter(lambda numb: numb != 0, lst))
    zeros: list = list(filter(lambda numb: numb == 0, lst))
    not_zeros_numbers.extend(zeros)
    return not_zeros_numbers