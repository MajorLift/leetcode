# Rotate Image
# https://leetcode.com/problems/rotate-image/
# Accepted 2023-04-07 19:56 UTC · Python · 36 ms · 13.8 MB

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        self.n = len(matrix)
        self.transpose()
        self.flip_vertical()

    def transpose(self):
        for i, j in product(range(self.n), range(self.n)):
            if i < j:
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
    
    def flip_vertical(self):
        for i in range(self.n):
            for j in range(self.n // 2):
                self.matrix[i][j], self.matrix[i][-(j + 1)] = self.matrix[i][-(j + 1)], self.matrix[i][j]
