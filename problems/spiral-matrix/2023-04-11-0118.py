# Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Accepted 2023-04-11 01:18 UTC · Python · 32 ms · 13.8 MB

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      nr, nc = len(matrix), len(matrix[0])
      i, j = 0, -1
      is_positive = True
      output = []
      while nr * nc > 0:
         for _ in range(nc):
            j += 1 if is_positive else -1
            output.append(matrix[i][j])
         nr -= 1
         for _ in range(nr):
            i += 1 if is_positive else -1
            output.append(matrix[i][j])
         nc -= 1
         is_positive = not is_positive
      return output
