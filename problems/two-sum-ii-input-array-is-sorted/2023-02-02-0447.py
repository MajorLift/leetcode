# Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted 2023-02-02 04:47 UTC · Python · 134 ms · 15 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        right = min(bisect_right(nums, max(target, target - nums[0])), len(nums) - 1)
        left = 0
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            if nums[left] + nums[right] < target:
                if nums[mid] + nums[right] < target:
                    left = mid
                else:
                    left += 1
            if nums[left] + nums[right] > target:
                if nums[left] + nums[mid] > target:
                    right = mid
                else:
                    right -= 1
