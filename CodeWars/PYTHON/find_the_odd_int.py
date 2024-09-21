"""
    Given an array of integers, find the one that appears an odd number of times.
    There will always be only one integer that appears an odd number of times.
"""

def find_it(seq):
    #6 kyu

    for number in seq:
        cnt_number: int = lambda x: seq.count(number)
        if cnt_number(number) % 2 != 0:
            return number
