# Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
# Accepted 2023-03-03 00:31 UTC · Python · 661 ms · 156.8 MB

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        @cache
        def dp(i, j):
            if j == m:
                return 1
            elif i == n:
                return 0
            elif s[i] == t[j]:
                return dp(i + 1, j + 1) + dp(i + 1, j)
            else:
                return dp(i + 1, j)
        return dp(0, 0)
