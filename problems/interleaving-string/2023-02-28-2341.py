# Interleaving String
# https://leetcode.com/problems/interleaving-string/
# Accepted 2023-02-28 23:41 UTC · Python · 37 ms · 15.1 MB

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        @cache
        def dp(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if i == len(s1) and j < len(s2):
                return s2[j] == s3[i + j] and dp(i, j + 1)
            if i < len(s1) and j == len(s2):
                return s1[i] == s3[i + j] and dp(i + 1, j)
            return (s1[i] == s3[i + j] and dp(i + 1, j)) \
                or (s2[j] == s3[i + j] and dp(i, j + 1))
        return dp(0, 0)
