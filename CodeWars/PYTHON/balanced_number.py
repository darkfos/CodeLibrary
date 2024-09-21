"""
    A balanced number is a number where the sum of digits to the left of the middle digit(s) and the sum of digits to the right of the middle digit(s) are equal.

    If the number has an odd number of digits, then there is only one middle digit. (For example, 92645 has one middle digit, 6.) Otherwise, there are two middle digits. (For example, the middle digits of 1301 are 3 and 0.)

    The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g. 413023 is a balanced number because the left sum and right sum are both 5.
    The task

    Given a number, find if it is balanced, and return the string "Balanced" or "Not Balanced" accordingly. The passed number will always be positive.

    7 ==> return "Balanced"
"""


def balanced_num(number):
    #7 kyu

    if len(str(number)) < 3:
        return "Balanced"
    else:
        center_number: int = len(str(number)) // 2
        ch_n: bool = False
        if len(str(number)) % 2 == 0:
            ch_n = True
        sm, sm2 = count_numbers(number, center_number, is_ch=ch_n)
        return "Balanced" if sm == sm2 else "Not Balanced"


def count_numbers(number: int, center_number: int, is_ch: True):
    if is_ch:
        sm: int = sum(map(lambda x1: int(x1), str(number)[:center_number-1]))
        sm2: int = sum(map(lambda y1: int(y1), str(number)[center_number+1:]))
    else:
        sm = sum(map(lambda x1: int(x1), str(number)[:center_number]))
        sm2 = sum(map(lambda x2: int(x2), str(number)[center_number+1:]))
    return sm, sm2