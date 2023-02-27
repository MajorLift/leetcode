# Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# Accepted 2023-02-27 22:30 UTC · Python · 170 ms · 55.1 MB

class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        @cache
        def dp(amount, idx):
            if amount == total: return 1
            if amount > total or idx <= 0: return 0
            return dp(amount, idx - 1) + dp(amount + coins[idx - 1], idx)
        return dp(0, len(coins))
