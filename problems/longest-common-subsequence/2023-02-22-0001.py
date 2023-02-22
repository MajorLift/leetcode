# Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# Accepted 2023-02-22 00:01 UTC · Python · 609 ms · 39.9 MB

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        text1, text2 = '0' + text1, '0' + text2
        memo = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                memo[i][j] = 1 + memo[i - 1][j - 1] \
                    if text1[i] == text2[j] \
                    else max(memo[i - 1][j], memo[i][j - 1])
        return memo[-1][-1]
