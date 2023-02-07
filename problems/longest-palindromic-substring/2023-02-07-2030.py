# Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Accepted 2023-02-07 20:30 UTC · Python · 470 ms · 13.9 MB

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return (r - 1) - (l + 1) + 1

        (start, end), global_max = (0, 0), 0
        for i in range(n):
            local_max = max(expand(i, i + 1), expand(i - 1, i + 1))
            (start, end), global_max = max(
                ((start, end), global_max), 
                ((i - (local_max - 1) // 2, i + local_max // 2), local_max) ,
                key=lambda x: x[1])
        return s[start:end + 1]
