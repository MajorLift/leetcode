# House Robber
# https://leetcode.com/problems/house-robber/
# Accepted 2022-10-19 21:55 UTC · Python · 50 ms · 13.9 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0, nums[0]] + [0] * (n - 1)
        for i in range(1, n):
            dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])
        return dp[-1]
