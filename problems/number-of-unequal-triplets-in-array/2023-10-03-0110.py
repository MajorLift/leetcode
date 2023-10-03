# Number of Unequal Triplets in Array
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/
# Accepted 2023-10-03 01:10 UTC · Python · 41 ms (90.73%) · 16.3 MB (25.87%)

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n, cnt = len(nums), Counter(nums)
        return math.comb(n, 3) - sum(math.comb(v, 2) * (n - v) + math.comb(v, 3) for v in cnt.values())
