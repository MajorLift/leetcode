# House Robber
# https://leetcode.com/problems/house-robber/
# Accepted 2023-02-04 03:47 UTC · Python · 32 ms · 13.8 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        return reduce(lambda acc, curr: (max(curr + acc[1], acc[0]), acc[0]), nums[::-1], (0, 0))[0]
