# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Accepted 2023-06-02 16:57 UTC · Python · 3494 ms · 18.2 MB

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            local_max = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    local_max = max(local_max, dp(j) + 1)
            return max(local_max, 1)
        return max(dp(i) for i in range(len(nums) - 1, -1, -1))
