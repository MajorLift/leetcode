# Number of Dice Rolls With Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# Accepted 2023-04-17 23:39 UTC · Python · 426 ms · 20.1 MB

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def backtrack(dice, rem):
            if dice == 0 and rem == 0:
                return 1
            return sum(backtrack(dice - 1, rem - i) 
                for i in range(1, k + 1) 
                if dice >= 1 and rem >= i)
        return backtrack(n, target) % MOD
