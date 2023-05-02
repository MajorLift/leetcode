# Sign of the Product of an Array
# https://leetcode.com/problems/sign-of-the-product-of-an-array/
# Accepted 2023-05-02 01:18 UTC · Python · 84 ms · 16.4 MB

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if any(e == 0 for e in nums):
            return 0
        return 1 if len(list(filter(lambda x: x < 0, nums))) % 2 == 0 else -1
