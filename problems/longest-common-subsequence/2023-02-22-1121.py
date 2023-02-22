# Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# Accepted 2023-02-22 11:21 UTC · Python · 657 ms · 40 MB

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        memo = [[0 for _ in range(n2)] for _ in range(n1)]
        for i in range(n1):
            for j in range(n2):
                memo[i][j] = 1 + (memo[i - 1][j - 1] if i * j > 0 else 0) \
                    if text1[i] == text2[j] \
                    else max(memo[i - 1][j] or 0, memo[i][j - 1] or 0)
        return memo[-1][-1]
