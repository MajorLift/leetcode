# Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/
# Accepted 2023-02-28 07:46 UTC · Python · 42 ms · 14.5 MB

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(remainder):
            if remainder == 0: return 1
            if remainder < 0: return 0
            return sum(dp(remainder - num) for num in nums)
        return dp(target)
