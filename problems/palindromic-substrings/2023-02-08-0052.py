# Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/
# Accepted 2023-02-08 00:52 UTC · Python · 323 ms · 22.7 MB

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        for l in range(n - 2, -1, -1):
            for r in range(l + 1, n):
                if s[l] == s[r] and (r - l <= 1 or memo[l + 1][r - 1]):
                    memo[l][r] += 1
        return sum(sum(row) for row in memo)
