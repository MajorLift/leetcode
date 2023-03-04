# Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
# Accepted 2023-03-04 02:39 UTC · Python · 594 ms · 71.3 MB

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = [[1 if j == n else 0 for j in range(n + 1)] for i in range(m + 1)]
        for i, j in product(range(m - 1, -1, -1), range(n - 1, -1, -1)):
            memo[i][j] = memo[i + 1][j] + (memo[i + 1][j + 1] 
                if s[i] == t[j]
                else 0)
        return memo[0][0]
