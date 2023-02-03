# House Robber II
# https://leetcode.com/problems/house-robber-ii/
# Accepted 2023-02-03 03:30 UTC · Python · 35 ms · 13.8 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        return max(reduce(lambda acc, curr: (max(curr + acc[1], acc[0]), acc[0]), arr, (0, 0))[0] for arr in (nums[:-1], nums[1:]))
