# Smallest Range I
# https://leetcode.com/problems/smallest-range-i/
# Accepted 2023-09-13 20:21 UTC · Python · 116 ms (32.1%) · 17.6 MB (87.81%)

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k)
