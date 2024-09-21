"""
    You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
"""


def sort_array(source_array):
    #6 kyu

    for number1 in range(len(source_array)):
        for number2 in range(len(source_array)):
            if source_array[number1] % 2 != 0 and source_array[number2] % 2 != 0:
                if source_array[number1] < source_array[number2]:
                    nmb1 = source_array[number1]
                    source_array[number1] = source_array[number2]
                    source_array[number2] = nmb1
    return source_array