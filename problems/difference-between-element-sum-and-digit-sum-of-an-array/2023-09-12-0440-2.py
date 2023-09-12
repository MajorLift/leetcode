# Difference Between Element Sum and Digit Sum of an Array
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
# Accepted 2023-09-12 04:40 UTC · Python · 119 ms · 16.6 MB

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def digit_iter(nums: List[int]):
            while nums:
                curr = nums.pop()
                yield curr % 10
                curr //= 10
                if curr:
                    nums.append(curr)
        return abs(sum(nums) - sum(digit_iter(nums)))
