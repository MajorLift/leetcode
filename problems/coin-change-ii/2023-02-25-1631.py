# Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# Accepted 2023-02-25 16:31 UTC · Python · 152 ms · 41.6 MB

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(i, j):
            if i == 0: return 1
            if j == 0: return 0
            return dp(i, j - 1) \
                + (dp(i - coins[j - 1], j) 
                    if coins[j - 1] <= i else 0)
        return dp(amount, len(coins))
