# N-Queens II
# https://leetcode.com/problems/n-queens-ii/
# Accepted 2022-06-03 05:03 UTC · Python · 706 ms · 14 MB

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.num_valid_boards = 0
        
        def backtrack(curr = (0, 0), 
                      queen_count = 1, 
                      search_space = [(i, j) for i in range(n) for j in range(n)]):
            # current square where the queen has been placed
            Qrow, Qcol = curr
            
            # base case: 
            # increment counter if valid board state with n queens has been reached
            if queen_count == n:
                self.num_valid_boards += 1
            
            # squares that are not under attack given the current configuration
            valid_squares = []
            # search space is restricted to valid squares from previous call
            for i, j in search_space:
                # excludes curr, and squares in its row, column, and diagonals.
                if i != Qrow and j != Qcol and abs((i - Qrow) / (j - Qcol)) != 1:
                    valid_squares.append((i, j))

            # visited nodes at the same level of the recursive tree are marked 
            # by being excluded from the search_space stack in subsequent calls
            while len(valid_squares):
                backtrack(valid_squares.pop(), queen_count + 1, valid_squares)
        
        # explore distinct first states
        for x in range(n):
            backtrack((0, x))

        return self.num_valid_boards
