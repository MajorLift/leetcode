# Minimum Suffix Flips
# https://leetcode.com/problems/minimum-suffix-flips/
# Accepted 2023-01-26 07:03 UTC · Python · 125 ms · 14.6 MB

class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        suffix = 0
        ans = 0
        for i in range(n):
            if target[i] != str(suffix):
                suffix = 1 - suffix
                ans += 1
        return ans
