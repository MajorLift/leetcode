# Paint House
# https://leetcode.com/problems/paint-house/
# Accepted 2023-02-04 02:19 UTC · Python · 74 ms · 14.3 MB

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp(i, color):
            if i < 0:
                return 0
            return costs[i][color] + min(dp(i - 1, (color + 1) % 3), dp(i - 1, (color + 2) % 3))
        return min(dp(len(costs) - 1, k) for k in range(3))
