# Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# Accepted 2023-02-22 00:05 UTC · Python · 942 ms · 140.7 MB

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        @cache
        def dp(i, j):
            if i < 0 or j < 0: return 0
            return 1 + dp(i - 1, j - 1) if text1[i] == text2[j] \
                else max(dp(i - 1, j), dp(i, j - 1))
        return dp(n1 - 1, n2 - 1)
