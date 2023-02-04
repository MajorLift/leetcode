# Paint House II
# https://leetcode.com/problems/paint-house-ii/
# Accepted 2023-02-04 02:21 UTC · Python · 214 ms · 15.4 MB

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        @cache
        def dp(i, color):
            if i < 0:
                return 0
            return costs[i][color] + min([dp(i - 1, j % k) 
                for j in range(color + 1, color + k)])
        return min([dp(n - 1, j) for j in range(k)])
