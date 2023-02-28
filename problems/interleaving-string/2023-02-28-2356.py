# Interleaving String
# https://leetcode.com/problems/interleaving-string/
# Accepted 2023-02-28 23:56 UTC · Python · 55 ms · 14.1 MB

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        memo = [([False] * (len(s2) + 1)) for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    memo[i][j] = True
                elif i == 0:
                    memo[i][j] = s2[j - 1] == s3[i + j - 1] and memo[i][j - 1]
                elif j == 0:
                    memo[i][j] = s1[i - 1] == s3[i + j - 1] and memo[i - 1][j]
                else:
                    memo[i][j] = s1[i - 1] == s3[i + j - 1] and memo[i - 1][j] \
                        or s2[j - 1] == s3[i + j - 1] and memo[i][j - 1]
        return memo[-1][-1]
