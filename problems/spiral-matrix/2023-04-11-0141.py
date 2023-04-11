# Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Accepted 2023-04-11 01:41 UTC · Python · 36 ms · 13.8 MB

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      matrix = deque([deque(row) for row in matrix])
      nr, nc = len(matrix), len(matrix[0])
      output = []
      while nr > 1 or nc > 1:
         print(matrix)
         if matrix:
            output.extend(matrix.popleft())
         nr -= 1

         print(matrix)
         for i in range(nr):
            if matrix[i]:
               output.append(matrix[i].pop())
         nc -= 1
         
         print(matrix)
         if matrix:
            output.extend(reversed(matrix.pop()))
            nr -= 1

         print(matrix)
         for i in range(nr - 1, -1, -1):
            if matrix[i]:
               output.append(matrix[i].popleft())
         nc -= 1
      
      print(matrix)
      if matrix:
         output.extend(matrix[0])
      print(matrix)
      return output
