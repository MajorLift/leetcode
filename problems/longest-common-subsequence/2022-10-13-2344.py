# Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# Accepted 2022-10-13 23:44 UTC · Python · 946 ms · 22.7 MB

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0 for j in range(n2 + 1)] for i in range(n1 + 1)]
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                dp[i][j] = 1 + dp[i + 1][j + 1] if text1[i] == text2[j] else max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
