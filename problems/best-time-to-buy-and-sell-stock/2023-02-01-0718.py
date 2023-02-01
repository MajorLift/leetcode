# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Accepted 2023-02-01 07:18 UTC · Python · 1092 ms · 24.9 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = +math.inf, -math.inf
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
