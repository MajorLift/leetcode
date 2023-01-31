# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Accepted 2023-01-31 04:14 UTC · Python · 63 ms · 16.7 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost += [0]
        @cache
        def dp(idx):
            if idx <= 1:
                return cost[idx]
            return cost[idx] + min(dp(idx - 1), dp(idx - 2))
        return dp(len(cost) - 1)
