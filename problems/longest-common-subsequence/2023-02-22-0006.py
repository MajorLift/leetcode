# Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# Accepted 2023-02-22 00:06 UTC · Python · 1027 ms · 141.1 MB

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        @cache
        def dp(i, j):
            if i >= n1 or j >= n2: return 0
            return 1 + dp(i + 1, j + 1) if text1[i] == text2[j] \
                else max(dp(i + 1, j), dp(i, j + 1))
        return dp(0, 0)
