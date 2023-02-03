# House Robber II
# https://leetcode.com/problems/house-robber-ii/
# Accepted 2023-02-03 03:24 UTC · Python · 41 ms · 13.8 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        candidates = nums[:-1], nums[1:]
        global_max = -math.inf
        for arr in candidates:
            acc = prev = 0
            for i in range(len(arr)):
                acc, prev = max(arr[i] + prev, acc), acc
            global_max = max(global_max, acc)
        return global_max
