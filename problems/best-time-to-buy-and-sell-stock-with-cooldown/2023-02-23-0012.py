# Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Accepted 2023-02-23 00:12 UTC · Python · 1334 ms · 14.2 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [0] * (n + 2)
        for buy in range(n - 2, -1, -1):
            memo[buy] = max(memo[buy + 1], 
                max(prices[sell] - prices[buy] + memo[sell + 2] 
                    for sell in range(buy + 1, n)))
        return memo[0]
