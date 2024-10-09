"""
    Your task is to write a function that receives as its single argument a string that
    contains numbers delimited by single spaces. Each number has a single alphabet
    letter somewhere within it.

    Example : "24z6 1x23 y369 89a 900b"

    As shown above, this alphabet letter can appear anywhere within the number. You have
    to extract the letters and sort the numbers according to their corresponding letters.

    Example : "24z6 1x23 y369 89a 900b" will become 89 900 123 369 246 (ordered according to the
    alphabet letter)

    Here comes the difficult part, now you have to do a series of computations on the numbers
    you have extracted.

    The sequence of computations are + - * /. Basic math rules do NOT apply, you have
    to do each computation in exactly this order.
    This has to work for any size of numbers sent in (after division, go back to addition, etc).
    In the case of duplicate alphabet letters, you have to arrange them according to the number
    that appeared first in the input string.
    Remember to also round the final answer to the nearest integer.
"""

def do_math(st):
    # 6kyu

    numbers: list = []
    for s_numb in st.split():
        number: str = ""
        alpha: str = ""
        for word in s_numb:
            if word.isalpha():
                alpha = word
            else:
                number += word
        numbers.append((alpha, number))


    result: int = 0
    cnt: int = 0

    numbers = sorted(numbers, key=lambda x: x[0])

    for op in numbers:
        if cnt == 5:
            cnt = 1

        match cnt:
            case 0:
                result += int(op[-1])
            case 1:
                result += int(op[-1])
            case 2:
                result -= int(op[-1])
            case 3:
                result *= int(op[-1])
            case 4:
                result /= int(op[-1])
        cnt += 1

    return round(result)