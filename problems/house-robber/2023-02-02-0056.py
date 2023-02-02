# House Robber
# https://leetcode.com/problems/house-robber/
# Accepted 2023-02-02 00:56 UTC · Python · 39 ms · 13.9 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i < 0:
                return 0
            return max(nums[i] + dp(i - 2), dp(i - 1))
        return dp(len(nums) - 1)
