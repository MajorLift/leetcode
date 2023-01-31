# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Accepted 2023-01-31 01:05 UTC · Python · 34 ms · 13.7 MB

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i <= 1:
                return 1
            return dp(i - 1) + dp(i - 2)
        return dp(n)
