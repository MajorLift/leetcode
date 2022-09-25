# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Accepted 2022-09-25 03:20 UTC · Python · 6026 ms · 14.3 MB

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            curr_max = -1
            for j in range(i):
                if nums[j] < nums[i] and dp[j] > curr_max:
                    curr_max = dp[j]
                    dp[i] = dp[j] + 1
        return max(dp)
