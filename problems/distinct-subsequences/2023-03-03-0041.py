# Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
# Accepted 2023-03-03 00:41 UTC · Python · 665 ms · 147.9 MB

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        @cache
        def dp(i, j):
            if j < 0:
                return 1
            elif i < 0:
                return 0
            elif s[i] == t[j]:
                return dp(i - 1, j - 1) + dp(i - 1, j)
            else:
                return dp(i - 1, j)
        return dp(n - 1, m - 1)
