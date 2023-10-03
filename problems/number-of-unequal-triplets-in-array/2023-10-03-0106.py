# Number of Unequal Triplets in Array
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/
# Accepted 2023-10-03 01:06 UTC · Python · 311 ms (73.94%) · 16.1 MB (85.14%)

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        return sum(x != y and y != z and z != x
            for x, y, z in combinations(nums, 3))
