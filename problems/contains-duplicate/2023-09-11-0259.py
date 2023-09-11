# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Accepted 2023-09-11 02:59 UTC · Python · 503 ms · 28.3 MB

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        return any(not nums[i - 1] ^ nums[i] for i in range(1, len(nums)))
