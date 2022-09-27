# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Accepted 2022-09-27 00:47 UTC · Python · 1090 ms · 25.1 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, minPrice = -math.inf, +math.inf
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit
