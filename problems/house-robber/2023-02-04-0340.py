# House Robber
# https://leetcode.com/problems/house-robber/
# Accepted 2023-02-04 03:40 UTC · Python · 27 ms · 13.9 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + dp(i + 2), dp(i + 1))
        return dp(0)
