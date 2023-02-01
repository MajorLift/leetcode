# Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
# Accepted 2023-02-01 04:41 UTC · Python · 140 ms · 14.8 MB

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        zeros = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.add((i, j))

        for r, c in zeros:
            for k in range(m):
                matrix[k][c] = 0
            for h in range(n):
                matrix[r][h] = 0
