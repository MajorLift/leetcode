# Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# Accepted 2023-02-01 04:00 UTC · Python · 101 ms · 13.9 MB

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for i in range(n):
            row_nums = [board[i][k] for k in range(n) if board[i][k] != "."]
            col_nums = [board[k][i] for k in range(n) if board[k][i] != "."]
            if len(row_nums) != len(set(row_nums)) or len(col_nums) != len(set(col_nums)):
                return False
        
        for i in range(3):
            for j in range(3):
                box_nums = []
                for k in range(3):
                    for h in range(3):
                        if board[i * 3 + k][j * 3 + h] != ".":
                            box_nums += board[i * 3 + k][j * 3 + h]
                if len(box_nums) != len(set(box_nums)):
                    return False
                    
        return True
