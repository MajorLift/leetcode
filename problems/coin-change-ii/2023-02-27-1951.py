# Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# Accepted 2023-02-27 19:51 UTC · Python · 553 ms · 34.7 MB

class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        memo = [([1] + [0] * total) for idx in range(len(coins))]
        for idx in range(len(coins)):
            for amount in range(1, total + 1):
                memo[idx][amount] += memo[idx - 1][amount]
                if amount >= coins[idx - 1]:
                    memo[idx][amount] += memo[idx][amount - coins[idx - 1]]
        return memo[-1][-1]
