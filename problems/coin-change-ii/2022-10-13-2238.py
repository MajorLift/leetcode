# Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# Accepted 2022-10-13 22:38 UTC · Python · 283 ms · 13.9 MB

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0 for _ in range(amount)]
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]
