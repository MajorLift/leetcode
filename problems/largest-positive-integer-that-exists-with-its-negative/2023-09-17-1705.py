# Largest Positive Integer That Exists With Its Negative
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
# Accepted 2023-09-17 17:05 UTC · Python · 111 ms (93.64%) · 16.5 MB (77.24%)

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums_set = set(nums)
        return max([num for num in nums_set
                    if num > 0 and -num in nums_set] 
                or [-1])
