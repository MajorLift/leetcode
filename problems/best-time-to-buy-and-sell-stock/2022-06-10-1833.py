# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Accepted 2022-06-10 18:33 UTC · Python · 1312 ms · 25.1 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price - min_price > max_profit:
                max_profit = price - min_price
            if price < min_price:
                min_price = price
        return max_profit
