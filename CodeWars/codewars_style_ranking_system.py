"""
    The objective is to return all pairs of integers from a given array of integers that have a difference of 2.

    The result array should be sorted in ascending order of values.

    Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter.
"""


def twos_difference(lst):
    # 6 kyu

    lst_answer: list = []

    for number1 in lst:
        for number2 in lst:
            if number1 - number2 in (0, -2) and number1 != number2:
                if number1 < number2:
                    res = (number1, number2)
                else:
                    res = (number2, number1)

                lst_answer.append(res)
                break
    return sorted(lst_answer)


print(twos_difference([1, 2, 3, 4]))