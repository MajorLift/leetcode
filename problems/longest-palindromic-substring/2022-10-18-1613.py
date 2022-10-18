# Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Accepted 2022-10-18 16:13 UTC · Python · 1433 ms · 13.8 MB

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = end = 0

        def expand(left, right):
            l, r = left, right
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        for i in range(n):
            curr_maxlen = max(expand(i, i), expand(i, i + 1))
            if curr_maxlen > end - start:
                start = i - (curr_maxlen - 1) // 2
                end = i + curr_maxlen // 2

        return s[start:end+1]
