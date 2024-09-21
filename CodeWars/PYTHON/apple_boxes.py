"""
    There're k square apple boxes full of apples. If a box is of size m, then it contains m × m apples. You noticed two interesting properties about the boxes:

    The smallest box is of size 1,
    the next one is of size 2,...,
    all the way up to size k.

    Boxes that have an odd size contain only yellow apples.
    Boxes that have an even size contain only red apples.

    Your task is to calculate the difference between the number of red apples and the number of yellow apples.
"""


def apple_boxes(k):
    #7 kyu

    yellow_apple: int = 0
    red_apple: int = 0
    for box in range(1, k+1):
        if box % 2 == 0:
            red_apple += box**2
        else:
            yellow_apple += box**2
    return red_apple - yellow_apple