# Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted 2023-02-02 04:54 UTC · Python · 116 ms · 14.9 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            while nums[left] + nums[right] < target:
                left = max(left + 1, 
                    bisect_left(nums, target - nums[right], 
                        lo=left + 1, hi=right - 1))
            while nums[left] + nums[right] > target:
                right = min(right - 1, 
                    bisect_right(nums, target - nums[left], 
                        lo=left + 1, hi=right - 1))
