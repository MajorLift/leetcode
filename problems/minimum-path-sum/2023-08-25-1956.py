# Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/
# Accepted 2023-08-25 19:56 UTC · Python · 117 ms · 22.4 MB

class Solution:
    def minPathSum(self, grid: List[List[int]]):
        m, n = map(len, (grid, grid[0]))
        START, END = (0, 0), (m - 1, n - 1)

        @cache
        def dp(i, j):
            curr_sum = 0
            if not (0 <= i < m and 0 <= j < n):
                return 0
            elif i == 0 and j == 0:
                curr_sum = grid[i][j]
            elif i == 0:
                curr_sum = grid[i][j] + dp(i, j - 1)
            elif j == 0:
                curr_sum = grid[i][j] + dp(i - 1, j)
            else:
                curr_sum = grid[i][j] + min(dp(i - 1, j), dp(i, j - 1))
            return curr_sum

        return dp(m - 1, n - 1)
