# Paint House
# https://leetcode.com/problems/paint-house/
# Accepted 2023-01-28 07:03 UTC · Python · 165 ms · 14.4 MB

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        @cache
        def dp(idx, color):
            if idx == n:
                return 0
            return costs[idx][color] + min(dp(idx + 1, (color + 1) % 3), dp(idx + 1, (color + 2) % 3))
        return min(dp(0, 0), dp(0, 1), dp(0, 2))
