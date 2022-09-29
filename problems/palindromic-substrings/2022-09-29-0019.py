# Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/
# Accepted 2022-09-29 00:19 UTC · Python · 426 ms · 72.6 MB

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[None for i in range(n)] for j in range(n)]
        
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        return len([(i, j) for i in range(n) for j in range(n) if dp[i][j]])
