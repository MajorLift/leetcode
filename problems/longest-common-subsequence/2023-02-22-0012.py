# Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/
# Accepted 2023-02-22 00:12 UTC · Python · 552 ms · 13.8 MB

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        shorter, longer = sorted([text1, text2], key=lambda x: len(x))
        n1, n2 = len(shorter), len(longer)
        prev, curr = [0] * (n1 + 1), [0] * (n1 + 1)
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                curr[j] = 1 + prev[j - 1] if shorter[j - 1] == longer[i - 1] \
                    else max(prev[j], curr[j - 1])
            prev, curr = curr, prev
        return prev[-1]
