# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Accepted 2023-02-01 05:46 UTC · Python · 237 ms · 24 MB

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = list(accumulate(nums, operator.mul))
        suffix = list(accumulate(nums[::-1], operator.mul))[::-1]
        return [suffix[1]] \
            + [prefix[i - 1] * suffix[i + 1] for i in range(1, len(nums) - 1)] \
            + [prefix[-2]]
