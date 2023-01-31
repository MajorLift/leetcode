# House Robber
# https://leetcode.com/problems/house-robber/
# Accepted 2023-01-31 04:25 UTC · Python · 32 ms · 13.9 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            return max(nums[i] + dp(i - 2), dp(i - 1)) if i >= 0 else 0
        return dp(len(nums) - 1)
