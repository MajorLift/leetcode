# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Accepted 2023-01-17 22:36 UTC · Python · 800 ms · 28.6 MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max, local_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            local_max = max(local_max, 0) + nums[i]
            global_max = max(global_max, local_max)
        return global_max
