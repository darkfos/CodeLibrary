class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Easy
        
        result: list = [0 for _ in range(len(s))]

        for indx, el in enumerate(indices):
            result[el] = s[indx]
        return "".join(result)