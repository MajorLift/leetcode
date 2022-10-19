# Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/
# Accepted 2022-10-19 22:12 UTC · Python · 289 ms · 22.8 MB

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        return sum(len([x for x in row if x]) for row in dp)
