# Number of Unequal Triplets in Array
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/
# Accepted 2023-10-03 01:17 UTC · Python · 435 ms (65.05%) · 16.1 MB (97.49%)

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return sum(cnt[i] * cnt[j] * cnt[k] 
            for i,j,k in combinations(cnt.keys(), 3))
