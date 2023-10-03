# Number of Unequal Triplets in Array
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/
# Accepted 2023-10-03 01:17 UTC · Python · 530 ms (22.2%) · 16.3 MB (58.88%)

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return sum(cnt[i] * cnt[j] * cnt[k] 
            for i, j, k in combinations(cnt.keys(), 3))
