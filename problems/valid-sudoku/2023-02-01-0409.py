# Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# Accepted 2023-02-01 04:09 UTC · Python · 112 ms · 14 MB

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_nums, col_nums = [], []
            for j in range(9):
                if board[i][j] != ".":
                    row_nums += board[i][j]
                if board[j][i] != ".":
                    col_nums += board[j][i]
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
