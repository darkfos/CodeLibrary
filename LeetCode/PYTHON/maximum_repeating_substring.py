"""
    For a string sequence, a string word is k-repeating if word concatenated k times is
    a substring of sequence. The word's maximum k-repeating value is the highest value
    k where word is k-repeating in sequence. If word is not a substring of sequence,
    word's maximum k-repeating value is 0.

    Given strings sequence and word, return the maximum k-repeating value of word in sequence.
"""

class Solution:
    # Easy
    def maxRepeating(self, sequence: str, word: str) -> int:
        sequence_start = sequence
        result: int = 0
        result_strings: list[str] = []
        while word in sequence:
            sequence = sequence.replace(word, "", 1)
            result += 1
            result_strings.append(word*result)

        for mx in result_strings[::-1]:
            if mx in sequence_start:
                return result_strings.index(mx)+1
        return 0