# Single Number
# https://leetcode.com/problems/single-number/
# Accepted 2023-04-12 18:58 UTC · Python · 135 ms · 16.9 MB

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda acc, curr: acc ^ curr, nums)
