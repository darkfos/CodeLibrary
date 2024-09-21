"""
    Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since
    James doesn't know how to make this happen, he needs your help.
    Task

    You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*)
    characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

    Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond
    of even or negative size.
"""


def diamond(n):
    # 6 kyu

    if n < 0 or n % 2 == 0:
        return None

    if n == 1:
        return "*\n"

    result_string: str = ""

    for start in range(n-1):
        if start % 2 != 0:
            result_string += " " * ((n - start) // 2)
            result_string += "*" * start
            result_string += "\n"

    for end in range(n, 0, -1):
        if end % 2 != 0:
            result_string += " " * ((n - end) // 2)
            result_string += "*" * end
            result_string += "\n"

    return result_string