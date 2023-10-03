# Number of Unequal Triplets in Array
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/
# Accepted 2023-10-03 01:00 UTC · Python · 316 ms (73.55%) · 16.1 MB (97.49%)

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        return sum(1 
            for x, y, z in combinations(nums, 3) 
            if x != y and y != z and z != x)
