# Paint House
# https://leetcode.com/problems/paint-house/
# Accepted 2023-02-03 07:14 UTC · Python · 77 ms · 14.3 MB

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @cache
        def dp(i, color):
            if i == len(costs):
                return 0
            return costs[i][color] + min(dp(i + 1, (color + 1) % 3), dp(i + 1, (color + 2) % 3))
        return min(dp(0, k) for k in range(3))
