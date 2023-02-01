# Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted 2023-02-01 21:23 UTC · Python · 151 ms · 14.9 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        right = bisect_left(nums, target)
        for j in range(min(right + 1, len(nums) - 1), 0, -1):
            for i in range(j):
                if nums[i] + nums[j] == target:
                    return [i + 1, j + 1]
