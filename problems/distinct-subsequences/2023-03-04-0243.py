# Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
# Accepted 2023-03-04 02:43 UTC · Python · 292 ms · 14.1 MB

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = [0] * n
        for i in range(m - 1, -1, -1):
            prev = 1
            for j in range(n - 1, -1, -1):
                tmp = memo[j]
                if s[i] == t[j]:
                    memo[j] += prev
                prev = tmp
        return memo[0]
