# Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/
# Accepted 2023-09-13 05:03 UTC · Python · 19 ms (100%) · 16.3 MB (26.32%)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(math.comb(k, 2) for k in Counter(nums).values())
