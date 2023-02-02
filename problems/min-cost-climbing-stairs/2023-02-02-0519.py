# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Accepted 2023-02-02 05:19 UTC · Python · 69 ms · 16.8 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost += [0]
        @cache
        def dp(i):
            if i <= 1:
                return cost[i]
            return cost[i] + min(dp(i - 1), dp(i - 2))
        return dp(len(cost) - 1)
