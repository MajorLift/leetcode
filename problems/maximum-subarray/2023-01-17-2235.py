# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Accepted 2023-01-17 22:35 UTC · Python · 781 ms · 28.6 MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        global_max = nums[0]
        last_max = nums[0]
        for i in range(1, n):
            last_max = max(last_max, 0) + nums[i]
            global_max = max(global_max, last_max)
        return global_max
