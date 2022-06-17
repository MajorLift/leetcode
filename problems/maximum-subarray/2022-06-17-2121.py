# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Accepted 2022-06-17 21:21 UTC · Python · 801 ms · 27.9 MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] + [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
        return max(dp)
