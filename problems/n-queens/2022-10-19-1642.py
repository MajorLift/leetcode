# N-Queens
# https://leetcode.com/problems/n-queens/
# Accepted 2022-10-19 16:42 UTC · Python · 1302 ms · 14.4 MB

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        template = [["." for _ in range(n)] for _ in range(n)]
        valid_init = [[True for _ in range(n)] for _ in range(n)]

        def backtrack(path = [0], row = 0, valid = valid_init):
            if row == n - 1:
                res = copy.deepcopy(template)
                for i, j in enumerate(path):
                    res[i][j] = "Q"
                row = ["".join(r) for r in res]
                output.append(row)
                return

            new_valid = copy.deepcopy(valid)
            for x in range(n):
                new_valid[row][x] = False # row
                new_valid[x][path[row]] = False # col
                if row + x < n:
                    if path[row] + x < n: # diag
                        new_valid[row + x][path[row] + x] = False
                    if path[row] - x >= 0: # anti-diag
                        new_valid[row + x][path[row] - x] = False
            for k in range(n):
                if new_valid[row + 1][k]:
                    backtrack(path + [k], row + 1, new_valid)

        for i in range(n):
            backtrack([i])
        return output
