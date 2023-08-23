# Candy Crush
# https://leetcode.com/problems/candy-crush/
# Accepted 2023-08-23 15:49 UTC · Python · 328 ms · 16.6 MB

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
      self.m, self.n = map(len, (board, board[0]))
      self.board = board
      while True:
        self.find()
        self.crush()
        if self.is_stable:
          return self.board
        self.drop()

    def find(self):
      self.is_stable = True

      for i in range(self.m):
        l = r = cnt = 0
        while l < self.n:
          while r < self.n and abs(self.board[i][l]) == abs(self.board[i][r]) > 0:
            cnt += 1
            r += 1
          if cnt >= 3:
            self.is_stable = False
            for k in range(l, r):
              self.board[i][k] = -abs(self.board[i][k])
          l = r = max(l + 1, r)
          cnt = 0

      for j in range(self.n):
        l = r = cnt = 0
        while l < self.m:
          while r < self.m and abs(self.board[l][j]) == abs(self.board[r][j]) > 0:
            cnt += 1
            r += 1
          if cnt >= 3:
            self.is_stable = False
            for k in range(l, r):
              self.board[k][j] = -abs(self.board[k][j])
          l = r = max(l + 1, r)
          cnt = 0
      
    def crush(self):
      for i, j in product(range(self.m), range(self.n)):
        self.board[i][j] = self.board[i][j] if self.board[i][j] > 0 else 0
      
    def drop(self):
      for j in range(self.n):
        l = r = self.m - 1
        while r >= 0:
          if self.board[r][j] == 0:
            l = max(l, r)
          elif l >= 0:
            self.board[r][j], self.board[l][j] = self.board[l][j], self.board[r][j]
            l -= 1
          r -= 1
