# N-Queens
# https://leetcode.com/problems/n-queens/
# Accepted 2022-12-27 08:54 UTC · Python · 57 ms · 14.4 MB

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, diags, antidiags = set(), set(), set()
        output = []
        def backtrack(row, state):
            if row == n:
                output.append(["".join(row) for row in state])
                return
            for col in range(n):
                if col in cols or row - col in diags or row + col in antidiags:
                    continue
                cols.add(col)
                diags.add(row - col)
                antidiags.add(row + col)
                state[row][col] = "Q"

                backtrack(row + 1, state)
                
                state[row][col] = "."
                cols.remove(col)
                diags.remove(row - col)
                antidiags.remove(row + col)

        backtrack(0, [["." for _ in range(n)] for _ in range(n)])
        return output
