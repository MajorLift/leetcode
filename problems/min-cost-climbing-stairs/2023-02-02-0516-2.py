# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Accepted 2023-02-02 05:16 UTC · Python · 55 ms · 14 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        acc = prev = 0
        for i in range(len(cost)):
            acc, prev = cost[i] + min(acc, prev), acc
        return min(acc, prev)
