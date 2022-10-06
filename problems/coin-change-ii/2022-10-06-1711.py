# Coin Change II
# https://leetcode.com/problems/coin-change-ii/
# Accepted 2022-10-06 17:11 UTC · Python · 1778 ms · 35.2 MB

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[1 if j == 0 else 0 for j in range(amount + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j] + (dp[i][j - coins[i - 1]] if j >= coins[i - 1] else 0)
        return dp[-1][-1]
