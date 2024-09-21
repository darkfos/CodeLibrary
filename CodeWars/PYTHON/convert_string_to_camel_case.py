"""
    Complete the method/function so that it converts dash/underscore delimited words into camel casing.
    The first word within the output should be capitalized only if the original word was capitalized
    (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
"""


def to_camel_case(text):
    #6 kyu

    new_text: str = ""
    flag: bool = False
    for ch in text:
        if ch in ("_", "-"):
            flag = True
            continue
        if flag:
            new_text += ch.upper()
            flag = False
        else:
            new_text += ch
    return new_text