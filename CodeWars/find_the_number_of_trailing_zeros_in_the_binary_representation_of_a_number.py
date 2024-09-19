def trailing_zeros(n) -> int:
    # 7 kyu
    """
    Given a number n, find the number of trailing zeros in its binary representation.

    Examples:

    4  ->  2, because 4 is represented as 100
    5  ->  0, because 5 is represented as 101
    """

    number = bin(n)[2:]
    cnt: int = 0

    for el in number[::-1]:
        if el == "0":
            cnt += 1
        else:
            break

    return cnt