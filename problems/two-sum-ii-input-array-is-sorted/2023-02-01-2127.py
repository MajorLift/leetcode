# Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted 2023-02-01 21:27 UTC · Python · 110 ms · 14.8 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        right = min(bisect_left(nums, target) + 1, len(nums) - 1)
        for j in range(right, 0, -1):
            i = max(bisect_right(nums[:j], target - nums[j]) - 1, 0)
            if nums[i] + nums[j] == target:
                return [i + 1, j + 1]
