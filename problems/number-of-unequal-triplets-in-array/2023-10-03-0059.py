# Number of Unequal Triplets in Array
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/
# Accepted 2023-10-03 00:59 UTC · Python · 1525 ms (5.01%) · 16.2 MB (85.14%)

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        return sum(1 
            for triplet in combinations(nums, 3) 
            if all(l != r for l, r in combinations(triplet, 2)))
