# Number of Unequal Triplets in Array
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/
# Accepted 2023-10-03 00:57 UTC · Python · 322 ms (73.36%) · 16.2 MB (58.88%)

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        return sum(1 
            for i, j, k in combinations(nums, 3) 
            if i != j and j != k and k != i)
