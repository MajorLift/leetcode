# Difference Between Element Sum and Digit Sum of an Array
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
# Accepted 2023-09-12 04:37 UTC · Python · 175 ms · 16.5 MB

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digit_iter(num: int):
            while num:
                pos = 10 ** int(math.log10(num))
                yield num // pos
                num -= (num // pos) * pos
        return abs(sum(nums) - sum(map(lambda num: sum(digit_iter(num)), nums)))
