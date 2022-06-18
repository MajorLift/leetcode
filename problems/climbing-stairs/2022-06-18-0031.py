# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Accepted 2022-06-18 00:31 UTC · Python · 46 ms · 13.9 MB

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
