# N-Queens II
# https://leetcode.com/problems/n-queens-ii/
# Accepted 2022-06-03 04:34 UTC · Python · 529 ms · 14 MB

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.output = 0
        
        def backtrack(curr = (0, 0), 
                      queen_count = 1, 
                      search_space = [(i, j) for i in range(n) for j in range(n)]):
            
            Qrow, Qcol = curr
            
            if queen_count == n:
                self.output += 1
                
            valid_squares = []
            for i, j in search_space:
                if i != Qrow and j != Qcol and abs((i - Qrow) / (j - Qcol)) != 1:
                    valid_squares.append((i, j))

            while(len(valid_squares)):
                backtrack(valid_squares.pop(), queen_count + 1, valid_squares)
        
        for x in range(n):
            backtrack((0, x))

        return self.output
