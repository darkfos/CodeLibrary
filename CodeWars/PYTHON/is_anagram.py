"""
    An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

    Note: anagrams are case insensitive

    Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
"""

def is_anagram(test, original):
    #7 kyu

    if len(test) != len(original): return False

    test: str = test.lower()
    original: str = original.lower()

    cnt: int = 0
    for j in test:
        if j in original:
            cnt += 1

    return cnt in (len(test), len(original))