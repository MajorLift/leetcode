# Coin Change
# https://leetcode.com/problems/coin-change/
# Accepted 2023-02-10 01:14 UTC · Python · 1801 ms · 14.3 MB

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [0.0] + [+math.inf for _ in range(amount)]
        for i in range(1, amount + 1):
            for coin in coins:
                memo[i] = min(memo[i], memo[i - coin] + 1 if i - coin >= 0 else +math.inf)
        return -1 if memo[amount] == +math.inf else int(memo[amount])
