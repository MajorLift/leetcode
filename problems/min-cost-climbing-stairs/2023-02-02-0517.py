# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Accepted 2023-02-02 05:17 UTC · Python · 52 ms · 14.1 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        acc = prev = 0
        for i in range(len(cost) - 1, -1, -1):
            acc, prev = cost[i] + min(acc, prev), acc
        return min(acc, prev)
