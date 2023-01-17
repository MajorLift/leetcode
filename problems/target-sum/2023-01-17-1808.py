# Target Sum
# https://leetcode.com/problems/target-sum/
# Accepted 2023-01-17 18:08 UTC · Python · 255 ms · 39.3 MB

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(idx = len(nums) - 1, curr = 0):
            if idx < 0: 
                return 1 if curr == target else 0
            return dp(idx - 1, curr + nums[idx - 1]) + dp(idx - 1, curr - nums[idx - 1])
        return dp()
