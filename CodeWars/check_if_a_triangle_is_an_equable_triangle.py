"""
    A triangle is called an equable triangle if its area equals its perimeter. Return true,
    if it is an equable triangle, else return false. You will be provided with the length of sides of the triangle.
    Happy Coding!
"""


def equable_triangle(a,b,c):
    #7 kyu

    per: int = (a+b+c) / 2
    s: int = ((per*(per-a)*(per-b)*(per-c)) ** 0.5) / 2
    return per == s