# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Accepted 2023-01-31 04:19 UTC · Python · 68 ms · 16.7 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost += [0]
        @cache
        def dp(idx):
            return cost[idx] + (min(dp(idx - 1), dp(idx - 2)) if idx > 1 else 0)
        return dp(n)
