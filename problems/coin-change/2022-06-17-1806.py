# Coin Change
# https://leetcode.com/problems/coin-change/
# Accepted 2022-06-17 18:06 UTC · Python · 2466 ms · 14.2 MB

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') if i > 0 else 0 for i in range(amount + 1)]
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - coin] + 1 \
                         if i - coin >= 0 else float('inf') \
                         for coin in coins])
        return [dp[amount], -1][dp[amount] == float('inf')]
