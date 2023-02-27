# Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# Accepted 2023-02-27 19:41 UTC · Python · 167 ms · 55 MB

class Solution:
    def change(self, total: int, coins: List[int]) -> int:
        @cache
        def dp(amount, idx):
            if amount < 0 or idx <= 0: return 0
            if amount == 0: return 1
            return dp(amount, idx - 1) + dp(amount - coins[idx - 1], idx)
        return dp(total, len(coins))
