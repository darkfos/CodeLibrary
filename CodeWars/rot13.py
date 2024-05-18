"""
    ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13
    letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

    Create a function that takes a string and returns the string ciphered with Rot13.
    If there are numbers or special characters included in the string, they should be returned as they are.
    Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
"""


def rot13(message):
    #5 kyu

    letters: tuple = tuple(chr(ch) for ch in range(97, 123)) * 2
    new_message: str = ""

    for ch in message:
        if ch.isalpha():
            flg: bool = True if ch.isupper() else False
            rng: int = letters.index(ch.lower())+13
            new_message += letters[letters.index(ch.lower())+13].upper() if flg else letters[letters.index(ch.lower())+13] if rng > 26 else letters[rng].upper() if flg else letters[rng]
        else:
            new_message += ch
    return new_message