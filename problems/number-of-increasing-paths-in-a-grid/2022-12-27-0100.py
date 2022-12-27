# Number of Increasing Paths in a Grid
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
# Accepted 2022-12-27 01:00 UTC · Python · 2597 ms · 89.1 MB

from functools import cache

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(r, c):
            return 1 + sum(dfs(i, j) if 0 <= i < m and 0 <= j < n and grid[i][j] > grid[r][c] else 0 \
                for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))) % MOD
        return sum(dfs(i, j) for i in range(m) for j in range(n)) % MOD
