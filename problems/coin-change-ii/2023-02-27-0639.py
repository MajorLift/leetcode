# Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# Accepted 2023-02-27 06:39 UTC · Python · 148 ms · 41.6 MB

class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        @cache
        def dp(coin_idx, amount):
            if coin_idx == 0: return 0
            if amount == 0: return 1
            return dp(coin_idx - 1, amount) \
                + (dp(coin_idx, amount - coins[coin_idx - 1]) 
                    if coins[coin_idx - 1] <= amount else 0)
        return dp(len(coins), total)
