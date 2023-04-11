# Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Accepted 2023-04-11 19:08 UTC · Python · 29 ms · 13.8 MB

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
