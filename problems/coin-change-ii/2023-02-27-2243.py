# Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# Accepted 2023-02-27 22:43 UTC · Python · 136 ms · 14.1 MB

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [1] + [0] * amount
        for coin in coins:
            for x in range(coin, amount + 1):
                memo[x] += memo[x - coin]
        return memo[-1]
