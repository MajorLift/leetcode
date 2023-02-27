# Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# Accepted 2023-02-27 22:46 UTC · Python · 181 ms · 55.1 MB

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(x, i):
            if x == amount: return 1
            if x > amount or i <= 0: return 0
            return dp(x, i - 1) + dp(x + coins[i - 1], i)
        return dp(0, len(coins))
