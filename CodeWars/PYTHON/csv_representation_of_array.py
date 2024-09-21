"""
    Create a function that returns the CSV representation of a two-dimensional numeric array.
    Array's length > 2.

    More details here: https://en.wikipedia.org/wiki/Comma-separated_values
    Note: you shouldn't escape the \n, it should work as a new line.
"""


def to_csv_text(array):
    #8 kyu

    array = list(map(lambda x: [str(numb) for numb in x], array))
    return "\\n".join(list(map(lambda arr: ",".join(arr), array)))