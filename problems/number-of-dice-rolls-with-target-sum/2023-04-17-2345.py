# Number of Dice Rolls With Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# Accepted 2023-04-17 23:45 UTC · Python · 380 ms · 20.6 MB

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def backtrack(dice, remainder):
            if dice > n or remainder < 0:
                return 0
            if dice == n and remainder == 0:
                return 1
            return sum(backtrack(dice + 1, remainder - i) 
                for i in range(1, k + 1))
        return backtrack(0, target) % MOD
