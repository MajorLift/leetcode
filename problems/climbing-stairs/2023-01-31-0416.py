# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Accepted 2023-01-31 04:16 UTC · Python · 26 ms · 13.8 MB

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            return dp(i - 1) + dp(i - 2) if i > 1 else 1
        return dp(n)
