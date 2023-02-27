# Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# Accepted 2023-02-27 19:45 UTC · Python · 137 ms · 14.1 MB

class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        memo = [1] + [0 for _ in range(total)]
        for coin in coins:
            for amount in range(coin, total + 1):
                memo[amount] += memo[amount - coin]
        return memo[-1]
