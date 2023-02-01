# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Accepted 2023-02-01 01:13 UTC · Python · 61 ms · 16.7 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost += [0]
        @cache
        def dp(i):
            if i <= 1:
                return cost[i]
            return cost[i] + min(dp(i - 1), dp(i - 2))
        return dp(n)
