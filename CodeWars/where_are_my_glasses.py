"""
    Oh no! I've lost my glasses, but paradoxically, I need glasses to find my glasses!

    Please help me out by showing me the index in the list which contains my glasses. They look like two capital Os,
    with at least one dash in between!
    This means that both O--O and O------------O are valid glasses, but not O----#--O for example!
    Search thoroughly, you might find my glasses in places such as 'dustO-Odust'

    Examples

        findGlasses(["phone", "O-O", "coins", "keys"]) ➞ 1    
        findGlasses(["OO", "wallet", "O##O", "O----O"]) ➞ 3
        findGlasses(["O--#--O", "dustO---Odust", "more dust"]) ➞ 1

    Notes

    All lists will include one valid pair of glasses because I swear I dropped them around here somewhere ...
    All elements in the list are strings.
"""

import re

def find_glasses(lst):
    #7 kyu

    find_glasses = re.compile(r"O[-]+O")
    for indx, el in enumerate(lst):
        is_find = re.search(find_glasses, el)
        if is_find:
            return indx