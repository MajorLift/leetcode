# Decode Ways
# https://leetcode.com/problems/decode-ways/
# Accepted 2023-02-09 02:51 UTC · Python · 41 ms · 14 MB

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [1, 0 if s[0] == "0" else 1] + [0 for _ in range(len(s) - 1)]
        for i in range(2, len(s) + 1):
            if s[i - 1] != "0":
                memo[i] = memo[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                memo[i] += memo[i - 2]
        return memo[-1]
