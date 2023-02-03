# House Robber
# https://leetcode.com/problems/house-robber/
# Accepted 2023-02-03 00:15 UTC · Python · 33 ms · 13.8 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        acc = prev = 0
        for i in range(len(nums)):
            acc, prev = max(nums[i] + prev, acc), acc
        return acc
