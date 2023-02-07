# Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Accepted 2023-02-07 22:29 UTC · Python · 474 ms · 14 MB

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return (r - 1) - (l + 1) + 1

        global_max, (start, end) = 0, (0, 0)
        for i in range(n):
            local_max = max(expand(i, i + 1), expand(i - 1, i + 1))
            global_max, (start, end) = max(
                (global_max, (start, end)), 
                (local_max, (i - (local_max - 1) // 2, i + local_max // 2)) ,
                key=lambda x: x[0])
        return s[start:end + 1]
