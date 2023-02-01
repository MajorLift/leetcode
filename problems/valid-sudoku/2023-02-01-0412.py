# Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# Accepted 2023-02-01 04:12 UTC · Python · 109 ms · 13.9 MB

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_nums = [board[i][j] for j in range(9) if board[i][j] != "."]
            col_nums = [board[j][i] for j in range(9) if board[j][i] != "."]
            if len(row_nums) != len(set(row_nums)) or len(col_nums) != len(set(col_nums)):
                return False
        
        for i in range(3):
            for j in range(3):
                box_nums = [board[i * 3 + k][j * 3 + h] for k in range(3) for h in range(3) if board[i * 3 + k][j * 3 + h] != "."]
                if len(box_nums) != len(set(box_nums)):
                    return False
                    
        return True
