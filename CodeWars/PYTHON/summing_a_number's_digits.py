"""
    Write a function named sumDigits
    which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits. 
"""

def sum_digits(number):
    #7 kyu

    return sum(map(lambda x: int(x) if x.isdigit() else 0, str(number)))