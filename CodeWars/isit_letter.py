"""
    Write a function, isItLetter or is_it_letter or IsItLetter,
    which tells us if a given character is a letter or not.
"""


def is_it_letter(s):
    #7 kyu

    wrds: str = "abcdefghijklmnopqrstuvwxyz"
    return s.lower() in wrds