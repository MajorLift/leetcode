# Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/
# Accepted 2023-01-26 18:25 UTC · Python · 103 ms · 14.3 MB

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(i, j):
            if j == len(p):
                return i == len(s)
            is_curr_match = i < len(s) and p[j] in (s[i], ".")
            if j < len(p) - 1 and p[j + 1] == "*":
                return dp(i, j + 2) or (is_curr_match and dp(i + 1, j))
            else:
                return is_curr_match and dp(i + 1, j + 1)
            return True
        return dp(0, 0)
