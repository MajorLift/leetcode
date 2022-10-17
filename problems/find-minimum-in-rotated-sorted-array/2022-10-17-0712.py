# Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Accepted 2022-10-17 07:12 UTC · Python · 94 ms · 14.1 MB

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                return nums[i]
        return nums[0]
