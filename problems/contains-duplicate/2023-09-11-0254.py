# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Accepted 2023-09-11 02:54 UTC · Python · 515 ms · 28.3 MB

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return any(l == r for l, r in zip(nums, nums[1:]))
