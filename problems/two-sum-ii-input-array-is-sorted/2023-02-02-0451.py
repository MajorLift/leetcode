# Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted 2023-02-02 04:51 UTC · Python · 133 ms · 14.9 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        right = min(bisect_right(nums, max(target, target - nums[0])), len(nums) - 1)
        left = 0
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            while nums[left] + nums[right] < target:
                left = max(bisect_left(nums, target - nums[right]), left + 1)
            while nums[left] + nums[right] > target:
                right = min(bisect_right(nums, target - nums[left]), right - 1)
