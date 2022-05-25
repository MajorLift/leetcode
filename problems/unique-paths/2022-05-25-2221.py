# Unique Paths
# https://leetcode.com/problems/unique-paths/
# Accepted 2022-05-25 22:21 UTC · Python · 45 ms · 13.9 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
        return memo[m - 1][n - 1]
