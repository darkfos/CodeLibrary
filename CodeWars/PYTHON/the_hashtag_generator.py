"""
    The marketing team is spending way too much time typing in hashtags.
    Let's help them with our own Hashtag Generator!

    Here's the deal:
    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.
"""


def generate_hashtag(s):
    # 5 kyu

    words: list = [word.title() for word in s.split(" ")]
    result: str = "".join(words)
    result: str = "#" + result
    if len(result) == 1: return False
    return result if 0 <= len(result) <= 140 else False