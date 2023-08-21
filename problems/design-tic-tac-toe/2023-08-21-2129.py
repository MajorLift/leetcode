# Design Tic-Tac-Toe
# https://leetcode.com/problems/design-tic-tac-toe/
# Accepted 2023-08-21 21:29 UTC · Python · 92 ms · 19.2 MB

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [None] * (n ** 2)

    def move(self, row: int, col: int, player: int) -> int:
        self.player = player
        self.board[row * self.n + col] = self.player
        # print(self.board, self.check_row(row), self.check_col(col), self.check_diags(row, col))
        if any([self.check_row(row), self.check_col(col), self.check_diags(row, col)]):
            return self.player
        return 0

    def check_row(self, row):
        return all(self.board[self.n * row + j] == self.player for j in range(self.n))

    def check_col(self, col):
        return all(self.board[self.n * i + col] == self.player for i in range(self.n))

    def check_diags(self, row, col):
        return (row == col and all(self.board[self.n * i + i] == self.player for i in range(self.n))) \
            or (col == self.n - 1 - row and all(self.board[self.n * i + self.n - 1 - i] == self.player for i in range(self.n)))
        
            

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
