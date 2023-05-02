# Number of Dice Rolls With Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# Accepted 2023-05-02 01:14 UTC · Python · 390 ms · 22.9 MB

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def backtrack(cnt=0, remaining=target):
            if cnt == n:
                return 1 if remaining == 0 else 0
            return sum(backtrack(cnt + 1, remaining - i) for i in range(1, k + 1))
        return backtrack() % MOD
