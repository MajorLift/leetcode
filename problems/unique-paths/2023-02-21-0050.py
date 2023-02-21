# Unique Paths
# https://leetcode.com/problems/unique-paths/
# Accepted 2023-02-21 00:50 UTC · Python · 36 ms · 13.8 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
        return memo[-1][-1]
