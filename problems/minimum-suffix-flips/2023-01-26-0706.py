# Minimum Suffix Flips
# https://leetcode.com/problems/minimum-suffix-flips/
# Accepted 2023-01-26 07:06 UTC · Python · 113 ms · 14.5 MB

class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        suffix = "0"
        ans = 0
        for bit in target:
            if bit != suffix:
                suffix = bit
                ans += 1
        return ans
