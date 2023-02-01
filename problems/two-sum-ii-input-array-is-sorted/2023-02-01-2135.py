# Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted 2023-02-01 21:35 UTC · Python · 112 ms · 14.9 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sup = min(bisect_left(nums, target) + 1, len(nums) - 1)
        for right in range(sup, 0, -1):
            left = bisect_right(nums[:right], target - nums[right]) - 1
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
