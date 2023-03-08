# Edit Distance
# https://leetcode.com/problems/edit-distance/
# Accepted 2023-03-08 19:59 UTC · Python · 76 ms · 17 MB

class Solution:
    def minDistance(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m == 0:
            return n
        if n == 0:
            return m
        s, t = "0" + s, "0" + t
        @cache
        def dp(i, j):
            if i * j == 0:
                return i + j
            elif s[i] == t[j]:
                return dp(i - 1, j - 1)
            return 1 + min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1))
        return dp(m, n)
