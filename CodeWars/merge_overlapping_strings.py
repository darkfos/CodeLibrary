"""
    This kata requires you to write a function which merges two strings together. It does so by merging the end
    of the first string with the start of the second string together when they are an exact match.

    "abcde" + "cdefgh" => "abcdefgh"
    "abaab" + "aabab" => "abaabab"
    "abc" + "def" => "abcdef"
    "abc" + "abc" => "abc"

    NOTE: The algorithm should always use the longest possible overlap.

    "abaabaab" + "aabaabab" would be "abaabaabab" and not "abaabaabaabab"
"""


def merge_strings(first, second):
    #7 kyu

    indx: int = -1
    mx: int = 0
    indx2: int = -1
    for ch in first[::-1]:
        if second.startswith(first[indx:]):
            mx_2 = len(first[indx:])
            if mx_2 > mx:
                mx = mx_2
                indx2 = indx
        indx -= 1
    if mx:
        return first[:indx2] + second
    return first+second