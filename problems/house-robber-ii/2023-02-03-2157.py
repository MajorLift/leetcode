# House Robber II
# https://leetcode.com/problems/house-robber-ii/
# Accepted 2023-02-03 21:57 UTC · Python · 32 ms · 14.2 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        candidates = nums[:-1], nums[1:]
        @cache
        def dp(c, i = 0):
            arr = candidates[c]
            if i >= len(nums) - 1:
                return 0
            return max(arr[i] + dp(c, i + 2), dp(c, i + 1))
        return max(dp(0), dp(1))
