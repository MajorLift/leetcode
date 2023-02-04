# House Robber
# https://leetcode.com/problems/house-robber/
# Accepted 2023-02-04 06:29 UTC · Python · 25 ms · 13.9 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1: return nums[0]
        memo = [0] * len(nums)
        for i in range(len(nums)):
            memo[i] = max(nums[i] + (memo[i - 2] or 0), (memo[i - 1] or 0))
        return memo[-1]
