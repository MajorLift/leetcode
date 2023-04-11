# Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Accepted 2023-04-11 19:07 UTC · Python · 32 ms · 13.8 MB

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      return matrix and [*matrix.pop(0)] + self.spiralOrder(self.rotate_ccw(matrix))

   def rotate_ccw(self, matrix: List[List[int]]):
      return matrix and self.compose(self.flip_vertical, self.antidiag_transpose)(matrix)

   def compose(self, *funcs):
      return reduce(lambda f, g: lambda x: f(g(x)), funcs)

   def flip_vertical(self, matrix: List[List[int]]):
      return [list(reversed(row)) for row in matrix]
   
   def antidiag_transpose(self, matrix: List[List[int]]):
      return [[row[j] for row in matrix[::-1]] for j in range(len(matrix[0]) - 1, -1, -1)]
