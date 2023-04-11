# Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Accepted 2023-04-11 03:43 UTC · Python · 24 ms · 14 MB

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      return matrix and [*matrix.pop(0)] + self.spiralOrder(self.rotate_ccw(matrix))

   def rotate_ccw(self, matrix: List[List[int]]):
      return matrix and self.transpose(self.reflect(matrix))

   def reflect(self, matrix: List[List[int]]):
      return matrix and [list(reversed(row)) for row in matrix]

   def transpose(self, matrix: List[List[int]]):
      return matrix and [[row[j] for row in matrix] for j in range(len(matrix[0]))]
