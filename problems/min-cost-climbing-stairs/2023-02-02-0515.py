# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Accepted 2023-02-02 05:15 UTC · Python · 57 ms · 14 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        acc, prev = 0, 0
        for i in range(n - 1, -1, -1):
            acc, prev = cost[i] + min(acc, prev), acc
        return min(acc, prev)
