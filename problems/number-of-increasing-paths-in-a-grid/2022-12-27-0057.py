# Number of Increasing Paths in a Grid
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
# Accepted 2022-12-27 00:57 UTC · Python · 2250 ms · 107.3 MB

from functools import cache

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(r, c):
            ans = 1
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] > grid[r][c]:
                    ans += dfs(i, j)
            return ans % MOD
        return sum(dfs(i, j) for i in range(m) for j in range(n)) % MOD
