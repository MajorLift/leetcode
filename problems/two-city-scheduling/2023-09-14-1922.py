# Two City Scheduling
# https://leetcode.com/problems/two-city-scheduling/
# Accepted 2023-09-14 19:22 UTC · Python · 51 ms (43.56%) · 16.1 MB (99.95%)

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x: x[0] - x[1])
        return sum(costs[i][i >= n] for i in range(2 * n))
