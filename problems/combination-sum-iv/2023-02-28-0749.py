# Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/
# Accepted 2023-02-28 07:49 UTC · Python · 44 ms · 13.7 MB

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [1] + [0] * target
        for x in range(1, target + 1):
            for num in nums:
                if x - num >= 0:
                    memo[x] += memo[x - num]
        return memo[-1]
