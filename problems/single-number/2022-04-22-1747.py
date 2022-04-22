# Single Number
# https://leetcode.com/problems/single-number/
# Accepted 2022-04-22 17:47 UTC · Python · 207 ms · 16.8 MB

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda curr, acc: acc ^ curr, nums, 0)
