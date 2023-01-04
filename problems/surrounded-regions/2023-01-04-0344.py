# Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/
# Accepted 2023-01-04 03:44 UTC · Python · 332 ms · 16.3 MB

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        if m <= 2 or n <= 2:
            return

        # mark uncapturable "O"s with temp value "B"
        def dfs(r, c):
            board[r][c] = "B"
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                    dfs(i, j)

        # find "O"s on border, and mark all connected squares as uncapturable regions.
        for i, j in [(i, 0) for i in range(m - 1)] + [(i, n - 1) for i in range(1, m)] \
            + [(0, j) for j in range(1, n)] + [(m - 1, j) for j in range(n - 1)]:
            if board[i][j] == "O":
                dfs(i, j)

        # All remaining "O"s can be surrounded. Flip to "X". Revert "B"s to "O"s. 
        for i, j in itertools.product(range(m), range(n)):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "B":
                board[i][j] = "O"
