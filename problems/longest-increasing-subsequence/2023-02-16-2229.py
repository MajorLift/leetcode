# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Accepted 2023-02-16 22:29 UTC · Python · 3785 ms · 16.3 MB

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i):
            local_max = -math.inf
            for j in range(i):
                if nums[i] > nums[j]:
                    local_max = max(local_max, dp(j) + 1)
            return local_max if local_max > -math.inf else 1
        return max(dp(i) for i in range(n))
