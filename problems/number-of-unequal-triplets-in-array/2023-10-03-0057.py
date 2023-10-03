# Number of Unequal Triplets in Array
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/
# Accepted 2023-10-03 00:57 UTC · Python · 514 ms (26.06%) · 16.3 MB (58.88%)

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        return sum(1 
            for i, j, k in combinations(range(len(nums)), 3) 
            if nums[i] != nums[j] 
                and nums[j] != nums[k] 
                and nums[k] != nums[i])
