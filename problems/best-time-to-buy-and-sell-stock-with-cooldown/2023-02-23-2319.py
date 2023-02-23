# Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Accepted 2023-02-23 23:19 UTC · Python · 47 ms · 18.3 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dp(i, doesBuy):
            if i >= n: return 0
            if doesBuy:
                return max(dp(i + 1, not doesBuy) - prices[i], dp(i + 1, doesBuy))
            else:
                return max(dp(i + 2, not doesBuy) + prices[i], dp(i + 1, doesBuy))
        return dp(0, True)
