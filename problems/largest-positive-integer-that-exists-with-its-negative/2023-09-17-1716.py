# Largest Positive Integer That Exists With Its Negative
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
# Accepted 2023-09-17 17:16 UTC · Python · 114 ms (86.95%) · 16.4 MB (77.24%)

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            if -nums[l] < nums[r]:
                r -= 1
            elif -nums[l] > nums[r]:
                l += 1
            else:
                return nums[r]
        return -1
