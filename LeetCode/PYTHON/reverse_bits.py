class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverse bits of a given 32 bits unsigned integer.
        Easy
        """

        return int('{:032b}'.format(n)[::-1], 2)