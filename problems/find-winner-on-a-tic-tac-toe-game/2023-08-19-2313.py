# Find Winner on a Tic Tac Toe Game
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
# Accepted 2023-08-19 23:13 UTC · Python · 31 ms · 16.2 MB

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        self.board = [[None] * 3 for _ in range(3)]
        self.player = True
        self.remaining = 9

        for r, c in moves:
            self.board[r][c] = self.player
            if any([self.check_rows(r), self.check_cols(c), self.check_diags(r, c)]):
                return 'A' if self.player else 'B'
            self.player = not self.player
            self.remaining -= 1
        
        return "Draw" if not self.remaining else "Pending"

    def check_rows(self, r):
        return all(self.board[r][j] == self.player for j in range(3))

    def check_cols(self, c):
        return all(self.board[i][c] == self.player for i in range(3))

    def check_diags(self, r, c):
        return r == c and all(self.board[i][i] == self.player for i in range(3)) \
            or c == 2 - r and all(self.board[i][2 - i] == self.player for i in range(3))
