# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Accepted 2023-09-11 03:08 UTC · Python · 497 ms · 28.5 MB

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return any(l == r for l, r in zip(nums, islice(nums, 1, None)))
