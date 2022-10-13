# Coin Change
# https://leetcode.com/problems/coin-change/
# Accepted 2022-10-13 22:29 UTC · Python · 1054 ms · 14.2 MB

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # output = []
        # def backtrack(tmp = [], remainder = amount):
        #     if remainder == 0:
        #         output.append(len(tmp))
        #     if remainder > 0:
        #         for coin in coins:
        #             backtrack(tmp + [coin], remainder - coin)
        # backtrack()
        # return min(output) if len(output) > 0 else -1
        
        dp = [0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - coin] + 1 if i >= coin else math.inf for coin in coins)
        return [dp[amount], -1][dp[amount] == math.inf]
