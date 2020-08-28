# Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
# Accepted 2020-08-28 12:38 UTC · Python · 136 ms · 14.3 MB

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        firstrow = matrix[0]
        firstcol = [matrix[i][0] for i in range(m)]
        
        for i,p in enumerate(matrix):
            if i == 0:
                pass
            for j,q in enumerate(matrix[i]):
                if j == 0:
                    pass
                if q == 0:
                    firstrow[j] = 0
                    firstcol[i] = 0

        for j,q in enumerate(firstrow):
            if j == 0:
                pass
            if q == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        for i,p in enumerate(firstcol):
            if p == 0:
                matrix[i] = [0]*n
