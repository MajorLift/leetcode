# Minimum Suffix Flips
# https://leetcode.com/problems/minimum-suffix-flips/
# Accepted 2023-01-26 07:02 UTC · Python · 142 ms · 14.6 MB

class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        suffix = "0"
        ans = 0
        for i in range(n):
            if target[i] != suffix:
                suffix = str(1 - int(suffix))
                ans += 1
        return ans
