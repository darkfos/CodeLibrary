"""
    Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

    Examples:

    foo -> foo1
    foobar23 -> foobar24
    foo0042 -> foo0043
    foo9 -> foo10
    foo099 -> foo100

    Attention: If the number has leading zeros the amount of digits should be considered.
"""


def increment_string(strng):
    #5 kyu

    digit: str = ""
    for ch in strng[::-1]:
        if ch.isdigit():
            digit += ch
        else:
            break
    
    if digit:
        digit2 = digit[::-1]
        digit = int(digit[::-1]) + 1
        if len(str(digit)) < len(digit2):
            return strng[:len(strng)-len(digit2)] + "0"*(len(digit2) - len(str(digit)))+str(digit)
        else:
            return strng[:len(strng)-len(digit2)] + str(digit)
    else:
        return strng + "1"