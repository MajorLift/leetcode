# House Robber
# https://leetcode.com/problems/house-robber/
# Accepted 2023-02-04 03:55 UTC · Python · 38 ms · 13.8 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        memo = [0] * len(nums)
        for i in range(len(nums)):
            memo[i] = max(nums[i] + memo[i - 2], memo[i - 1])
        return memo[-1]
