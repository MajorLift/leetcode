# Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/
# Accepted 2023-08-25 19:57 UTC · Python · 99 ms · 22.3 MB

class Solution:
    def minPathSum(self, grid: List[List[int]]):
        m, n = map(len, (grid, grid[0]))
        START, END = (0, 0), (m - 1, n - 1)

        @cache
        def dp(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return 0
            elif i == 0:
                return grid[i][j] + dp(i, j - 1)
            elif j == 0:
                return grid[i][j] + dp(i - 1, j)
            return grid[i][j] + min(dp(i - 1, j), dp(i, j - 1))

        return dp(m - 1, n - 1)
