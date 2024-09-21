"""
    Build Tower

    Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
    A tower block is represented with "*" character.
"""


def tower_builder(n_floors):
    #6 kyu

    cnt = 1
    lst: list = []
    cnt2 = 1
    for i in range(0, n_floors):
        ln = " "*(n_floors-cnt2)
        ln += "*"*cnt
        ln += " "*(n_floors-cnt2)
        cnt += 2
        cnt2 += 1
        lst.append(ln)
    return lst