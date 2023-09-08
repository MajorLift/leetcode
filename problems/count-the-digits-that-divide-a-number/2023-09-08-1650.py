# Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/
# Accepted 2023-09-08 16:50 UTC · Python · 29 ms · 16.4 MB

class Solution:
    def countDigits(self, num: int) -> int:
        return sum(1 for digit in str(num) if not num % int(digit))
