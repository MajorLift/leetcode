# Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Accepted 2023-01-17 18:47 UTC · Python · 53 ms · 14.2 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(n + 2)] for _ in range(2)]
        for i in range(n - 1, -1, -1):
            dp[0][i] = max(-prices[i] + dp[1][i + 1], dp[0][i + 1])
            dp[1][i] = max(prices[i] + dp[0][i + 2], dp[1][i + 1])  
        return dp[0][0]
