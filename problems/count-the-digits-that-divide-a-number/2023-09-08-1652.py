# Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/
# Accepted 2023-09-08 16:52 UTC · Python · 36 ms · 16.2 MB

class Solution:
    def countDigits(self, num: int) -> int:
        def digit_iter(num: int):
            while num:
                yield num % 10
                num //= 10
        return sum(1 for digit in digit_iter(num) if not num % digit)
