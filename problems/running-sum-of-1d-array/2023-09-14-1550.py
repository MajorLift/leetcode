# Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
# Accepted 2023-09-14 15:50 UTC · Python · 55 ms (24.45%) · 16.4 MB (81.63%)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)
