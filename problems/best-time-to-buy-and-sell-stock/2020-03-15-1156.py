# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Accepted 2020-03-15 11:56 UTC · Python · 64 ms · 14 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = float('inf'), 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit
