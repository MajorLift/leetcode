# Minimum Insertion Steps to Make a String Palindrome
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
# Accepted 2023-04-30 19:31 UTC · Python · 829 ms · 185.6 MB

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        @cache
        def dp(l, r):
            if l >= r:
                return 0
            if s[l] == s[r]:
                return dp(l + 1, r - 1)
            return 1 + min(dp(l + 1, r), dp(l, r - 1))
        return dp(0, n - 1)
