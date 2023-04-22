# Profitable Schemes
# https://leetcode.com/problems/profitable-schemes/
# Accepted 2023-04-22 00:55 UTC · Python · 4342 ms · 690 MB

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dp(i, spoils, idle):
            if idle < 0: 
                return 0
            if i == len(profit): 
                return int(spoils == minProfit)
            take = dp(i + 1, min(minProfit, spoils + profit[i]), idle - group[i])
            leave = dp(i + 1, spoils, idle)
            return take + leave
        return dp(0, 0, n) % MOD
