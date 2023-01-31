# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Accepted 2023-01-31 04:15 UTC · Python · 61 ms · 16.7 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost += [0]
        @cache
        def dp(idx):
            return cost[idx] + (min(dp(idx - 1), dp(idx - 2)) if idx > 1 else 0)
        return dp(len(cost) - 1)
