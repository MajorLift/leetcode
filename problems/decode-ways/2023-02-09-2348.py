# Decode Ways
# https://leetcode.com/problems/decode-ways/
# Accepted 2023-02-09 23:48 UTC · Python · 33 ms · 13.9 MB

class Solution:
    def numDecodings(self, s: str) -> int:
        acc, prev = 0 if s[0] == "0" else 1, 1
        for i in range(1, len(s)):
            acc, prev = (acc if s[i] != "0" else 0) + (prev if 10 <= int(s[i - 1:i + 1]) <= 26 else 0), acc
        return acc
