# Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Accepted 2023-02-23 23:25 UTC · Python · 53 ms · 18.4 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        BUY = True
        @cache
        def dp(i, transaction):
            if i >= n: return 0
            if transaction == BUY:
                return max(-prices[i] + dp(i + 1, not BUY), dp(i + 1, BUY))
            else:
                return max(+prices[i] + dp(i + 2, BUY), dp(i + 1, not BUY))
        return dp(0, BUY)
