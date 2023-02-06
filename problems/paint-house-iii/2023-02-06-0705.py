# Paint House III
# https://leetcode.com/problems/paint-house-iii/
# Accepted 2023-02-06 07:05 UTC · Python · 1240 ms · 34.9 MB

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def dp(i = 0, prev_color = 0, k = 0):
            if i == m and k == target:
                return 0
            if (i == m and k < target) or k > target:
                return +math.inf
            if houses[i] > 0:
                return dp(i + 1, houses[i], k + 1 if houses[i] != prev_color else k)
            return min(cost[i][color - 1] 
                + dp(i + 1, color, k + 1 if prev_color != color else k) 
                for color in range(1, n + 1))

        min_cost = dp() 
        return min_cost if min_cost < +math.inf else -1
