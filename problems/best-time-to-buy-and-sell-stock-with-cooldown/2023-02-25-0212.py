# Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Accepted 2023-02-25 02:12 UTC · Python · 44 ms · 14.2 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold, sold, rest = -math.inf, 0, 0
        for i in range(n):
            hold, sold, rest = max(hold, rest - prices[i]), hold + prices[i], max(rest, sold)
        return max(sold, rest)
