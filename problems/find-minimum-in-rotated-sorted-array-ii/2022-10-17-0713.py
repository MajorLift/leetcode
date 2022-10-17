# Find Minimum in Rotated Sorted Array II
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# Accepted 2022-10-17 07:13 UTC · Python · 109 ms · 14.5 MB

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                return nums[i]
        return nums[0]
