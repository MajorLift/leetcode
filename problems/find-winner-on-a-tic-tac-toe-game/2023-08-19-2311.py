# Find Winner on a Tic Tac Toe Game
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
# Accepted 2023-08-19 23:11 UTC · Python · 50 ms · 16.3 MB

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        self.board = [[None] * 3 for _ in range(3)]
        self.player = True
        self.remaining = 9
        for r, c in moves:
            self.board[r][c] = self.player
            if any([self.check_rows(r), self.check_cols(c), self.check_diags()]):
                return 'A' if self.player else 'B'
            self.player = not self.player
            self.remaining -= 1
        return "Draw" if not self.remaining else "Pending"

    def check_rows(self, r):
        return all(self.board[r][j] == self.player for j in range(3))

    def check_cols(self, c):
        return all(self.board[i][c] == self.player for i in range(3))

    def check_diags(self):
        return all(self.board[i][i] == self.player for i in range(3)) \
            or all(self.board[i][2 - i] == self.player for i in range(3))
