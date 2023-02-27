# Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# Accepted 2023-02-27 06:44 UTC · Python · 509 ms · 34.7 MB

class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        memo = [[1] + [0 for amount in range(total)] \
            for idx in range(len(coins))]
        for idx in range(len(coins)):
            for amount in range(total + 1):
                memo[idx][amount] = memo[idx - 1][amount] \
                    + (memo[idx][amount - coins[idx - 1]] 
                        if coins[idx - 1] <= amount else 0)
        return memo[-1][-1]
