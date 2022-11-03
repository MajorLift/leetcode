# Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Accepted 2022-11-03 19:03 UTC · Python · 915 ms · 14.8 MB

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(x, y):
            nonlocal matrix, dp
            if dp[x][y] > 0:
                return dp[x][y]
            for x_diff, y_diff in (0, 1), (1, 0), (-1, 0), (0, -1):
                r, c = x + x_diff, y + y_diff
                if (0 <= r < m and 0 <= c < n and matrix[r][c] > matrix[x][y]):
                    dp[x][y] = max(dp[x][y], dfs(r, c))
            dp[x][y] += 1
            return dp[x][y]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))           
        return ans
