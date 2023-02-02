# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Accepted 2023-02-02 05:33 UTC · Python · 62 ms · 13.9 MB

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      return min(functools.reduce(lambda acc, curr: (min(acc[0], acc[1]) + curr, acc[0]), cost, (0, 0)))
