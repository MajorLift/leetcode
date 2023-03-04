# Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
# Accepted 2023-03-04 02:34 UTC · Python · 595 ms · 71.6 MB

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        s, t = "0" + s, "0" + t
        memo = [[1 if j == 0 else 0 for j in range(n + 1)] for i in range(m + 1)]
        for i, j in product(range(1, m + 1), range(1, n + 1)):
            memo[i][j] = memo[i - 1][j] + (memo[i - 1][j - 1] 
                if s[i] == t[j]
                else 0)
        return memo[-1][-1]
