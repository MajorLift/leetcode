# Difference Between Element Sum and Digit Sum of an Array
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
# Accepted 2023-09-08 19:28 UTC · Python · 123 ms · 16.6 MB

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem_sum = sum(nums)
        digit_sum = 0
        while nums:
            curr = nums.pop()
            digit_sum += curr % 10
            curr //= 10
            if curr:
                nums.append(curr)
        return abs(elem_sum - digit_sum)
