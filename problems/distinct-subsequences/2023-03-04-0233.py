# Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
# Accepted 2023-03-04 02:33 UTC · Python · 702 ms · 71.4 MB

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = [[1 if j == 0 else 0 for j in range(n + 1)] for i in range(m + 1)]
        for i, j in product(range(1, m + 1), range(1, n + 1)):
            memo[i][j] = memo[i - 1][j] + (memo[i - 1][j - 1] 
                if s[i - 1] == t[j - 1]
                else 0)
        return memo[-1][-1]
