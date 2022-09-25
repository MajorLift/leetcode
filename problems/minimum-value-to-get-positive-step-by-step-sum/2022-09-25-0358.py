# Minimum Value to Get Positive Step by Step Sum
# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
# Accepted 2022-09-25 03:58 UTC · Python · 62 ms · 13.9 MB

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        cum_sums = [nums[0]] + [0] * (n - 1) 
        for i in range(1, n):
            cum_sums[i] = cum_sums[i - 1] + nums[i]
        min_val = min(cum_sums)
        return 1 - min_val if min_val < 0 else 1
