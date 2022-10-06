# Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# Accepted 2022-10-06 17:13 UTC · Python · 396 ms · 14.1 MB

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0 for _ in range(amount)]
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[-1]
