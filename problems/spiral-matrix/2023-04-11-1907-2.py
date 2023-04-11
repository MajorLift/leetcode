# Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Accepted 2023-04-11 19:07 UTC · Python · 35 ms · 13.9 MB

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      return matrix and [*matrix.pop(0)] + self.spiralOrder(self.rotate_ccw(matrix))

   def rotate_ccw(self, matrix: List[List[int]]):
      return matrix and self.compose(self.transpose, self.flip_vertical)(matrix)

   def compose(self, *funcs):
      return reduce(lambda f, g: lambda x: f(g(x)), funcs)

   def transpose(self, matrix: List[List[int]]):
      return [[row[j] for row in matrix] for j in range(len(matrix[0]))]

   def flip_vertical(self, matrix: List[List[int]]):
      return [list(reversed(row)) for row in matrix]
