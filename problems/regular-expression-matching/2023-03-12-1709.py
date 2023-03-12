# Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/
# Accepted 2023-03-12 17:09 UTC · Python · 48 ms · 13.9 MB

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = [[False] * (n + 1) for _ in range(m + 1)]
        memo[-1][-1] = True
        for i, j in product(range(m, -1, -1), range(n - 1, -1, -1)):
            is_curr_match = i < m and p[j] in (s[i], ".")
            if j < n - 1 and p[j + 1] == "*":
                memo[i][j] = memo[i][j + 2] or (is_curr_match and memo[i + 1][j])
            else:
                memo[i][j] = (is_curr_match and memo[i + 1][j + 1])
        return memo[0][0]
