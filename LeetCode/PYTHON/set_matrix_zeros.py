from typing import List

class Solution:
    # Medium
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zero_index: list = []
        for id_l, lst in enumerate(matrix):
            if 0 in lst:
                zero_index.extend([zero for zero in range(len(lst)) if lst[zero] == 0])
                matrix[id_l] = [0]*len(lst)
        for zero in zero_index:
            for id_l in range(len(matrix)):
                matrix[id_l][zero] = 0