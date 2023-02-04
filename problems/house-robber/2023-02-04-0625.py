# House Robber
# https://leetcode.com/problems/house-robber/
# Accepted 2023-02-04 06:25 UTC · Python · 35 ms · 13.9 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0] * (len(nums) + 2)
        for i in range(len(nums) - 1, -1, -1):
            memo[i] = max(nums[i] + memo[i + 2], memo[i + 1])
        return memo[0]
