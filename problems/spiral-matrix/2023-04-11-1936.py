# Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Accepted 2023-04-11 19:36 UTC · Python · 36 ms · 13.8 MB

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
      m, n = len(matrix), len(matrix[0])
      i = j = turns = 0
      blocked = False
      output = []
      while True:
         next_i, next_j = map(sum, zip((i, j), DIRECTIONS[turns % 4]))
         if not (0 <= next_i < m and 0 <= next_j < n) or matrix[next_i][next_j] == +inf:
            if blocked:
               output.append(matrix[i][j])
               break
            else:
               blocked = True
               turns += 1
               continue
         blocked = False
         output.append(matrix[i][j])
         matrix[i][j] = +inf
         i, j = next_i, next_j
      return output
