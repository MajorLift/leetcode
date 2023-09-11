# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Accepted 2023-09-11 02:53 UTC · Python · 473 ms · 30.9 MB

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
