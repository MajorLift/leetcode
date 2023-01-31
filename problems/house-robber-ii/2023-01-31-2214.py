# House Robber II
# https://leetcode.com/problems/house-robber-ii/
# Accepted 2023-01-31 22:14 UTC · Python · 36 ms · 14.1 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return max(nums)
        candidates = nums[:-1], nums[1:]
        @cache
        def dp(i, x):
            if i == 0:
                 return candidates[x][0]
            if i == 1:
                return max(candidates[x][:2])
            return max(candidates[x][i] + dp(i - 2, x), dp(i - 1, x))
        return max(dp(n - 2, 0), dp(n - 2, 1))
