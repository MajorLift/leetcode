# Interleaving String
# https://leetcode.com/problems/interleaving-string/
# Accepted 2023-03-01 23:45 UTC · Python · 56 ms · 14 MB

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        shorter, longer = sorted([s1, s2], key=len)
        memo = [False] * (len(shorter) + 1)
        for i in range(len(longer) + 1):
            for j in range(len(shorter) + 1):
                if i == 0 and j == 0:
                    memo[j] = True
                elif i == 0:
                    memo[j] = shorter[j - 1] == s3[i + j - 1] and memo[j - 1]
                elif j == 0:
                    memo[j] = longer[i - 1] == s3[i + j - 1] and memo[j]
                else:
                    memo[j] = longer[i - 1] == s3[i + j - 1] and memo[j] \
                        or shorter[j - 1] == s3[i + j - 1] and memo[j - 1]
        return memo[-1]
