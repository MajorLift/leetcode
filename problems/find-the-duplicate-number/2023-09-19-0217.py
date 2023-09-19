# Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/
# Accepted 2023-09-19 02:17 UTC · Python · 571 ms (28.82%) · 31 MB (55.79%)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]
