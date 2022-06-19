# Unique Paths
# https://leetcode.com/problems/unique-paths/
# Accepted 2022-06-19 08:37 UTC · Python · 39 ms · 13.9 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 if i * j > 0 else 1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
