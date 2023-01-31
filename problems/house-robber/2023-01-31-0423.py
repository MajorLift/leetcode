# House Robber
# https://leetcode.com/problems/house-robber/
# Accepted 2023-01-31 04:23 UTC · Python · 29 ms · 13.8 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[:2])
            return max(nums[i] + dp(i - 2), dp(i - 1))
        return dp(n - 1)
