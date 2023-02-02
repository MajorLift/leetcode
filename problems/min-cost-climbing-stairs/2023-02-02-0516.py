# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Accepted 2023-02-02 05:16 UTC · Python · 53 ms · 13.9 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        acc, prev = 0, 0
        for i in range(n):
            acc, prev = cost[i] + min(acc, prev), acc
        return min(acc, prev)
