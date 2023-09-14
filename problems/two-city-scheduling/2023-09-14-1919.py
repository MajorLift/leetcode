# Two City Scheduling
# https://leetcode.com/problems/two-city-scheduling/
# Accepted 2023-09-14 19:19 UTC · Python · 54 ms (31.59%) · 16.3 MB (85.77%)

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x: x[1] - x[0])
        return sum(costs[i][i < n] for i in range(2 * n))
