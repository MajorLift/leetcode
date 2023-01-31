# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Accepted 2023-01-31 01:01 UTC · Python · 41 ms · 13.8 MB

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i <= 2:
                return i
            return dp(i - 1) + dp(i - 2)
        return dp(n)
