# Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted 2023-02-02 04:52 UTC · Python · 113 ms · 15 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        # right = min(bisect_right(nums, max(target, target - nums[0])), len(nums) - 1)
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            while nums[left] + nums[right] < target:
                left = max(bisect_left(nums, target - nums[right], lo=left, hi=right), left + 1)
            while nums[left] + nums[right] > target:
                right = min(bisect_right(nums, target - nums[left], lo=left, hi=right), right - 1)
