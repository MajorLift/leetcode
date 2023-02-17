# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Accepted 2023-02-17 00:10 UTC · Python · 4006 ms · 16.2 MB

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i):
            local_max = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    local_max = max(local_max, dp(j) + 1)
            return local_max if local_max > 0 else 1
        return max(dp(i) for i in range(n))
