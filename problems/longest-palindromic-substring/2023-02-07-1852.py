# Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Accepted 2023-02-07 18:52 UTC · Python · 6373 ms · 22.8 MB

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = [[True if i == j else False for j in range(n)] for i in range(n)]
        max_idx = 0, 0
        for l in range(n - 2, -1, -1):
            for r in range(l + 1, n):
                if s[l] == s[r] and (r - l <= 1 or memo[l + 1][r - 1]):
                    memo[l][r] = True
                    max_idx = max(max_idx, (l, r), key=lambda x: x[1] - x[0])
        l, r = max_idx
        return s[l:r + 1]
