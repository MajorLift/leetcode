# Target Sum
# https://leetcode.com/problems/target-sum/
# Accepted 2023-02-28 00:49 UTC · Python · 265 ms · 39.1 MB

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, x):
            if i < 0: 
                return 1 if x == 0 else 0
            return dp(i - 1, x + nums[i]) + dp(i - 1, x - nums[i])
        return dp(len(nums) - 1, target)
