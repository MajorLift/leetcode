# Single Number
# https://leetcode.com/problems/single-number/
# Accepted 2022-10-28 15:51 UTC · Python · 303 ms · 17 MB

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 2) - sum(nums)
