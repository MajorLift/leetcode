# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Accepted 2023-02-01 01:20 UTC · Python · 68 ms · 13.9 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost += [0]
        acc, prev = cost[1], cost[0]
        for i in range(2, n + 1):
            acc, prev = cost[i] + min(acc, prev), acc
        return acc
