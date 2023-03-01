# Interleaving String
# https://leetcode.com/problems/interleaving-string/
# Accepted 2023-03-01 00:01 UTC · Python · 28 ms · 14.1 MB

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        @cache
        def dp(i, j):
            if i == 0 and j == 0:
                return True
            elif i == 0:
                return s2[j - 1] == s3[i + j - 1] and dp(i, j - 1)
            elif j == 0:
                return s1[i - 1] == s3[i + j - 1] and dp(i - 1, j)
            return (s1[i - 1] == s3[i + j - 1] and dp(i - 1, j)) \
                or (s2[j - 1] == s3[i + j - 1] and dp(i, j - 1))
        return dp(len(s1), len(s2))
