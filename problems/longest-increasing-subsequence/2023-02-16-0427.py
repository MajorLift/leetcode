# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Accepted 2023-02-16 04:27 UTC · Python · 3745 ms · 16.3 MB

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i):
            curr_max = -math.inf
            for j in range(i):
                if nums[i] > nums[j]:
                    curr_max = max(curr_max, dp(j) + 1)
            return curr_max if curr_max > -math.inf else 1
        return max(dp(i) for i in range(n))
