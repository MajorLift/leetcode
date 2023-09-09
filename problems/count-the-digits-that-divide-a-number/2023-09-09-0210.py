# Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/
# Accepted 2023-09-09 02:10 UTC · Python · 45 ms · 16.3 MB

class Solution:
    def countDigits(self, num: int) -> int:
        def digit_iter(num: int):
            while num:
                emax = 10 ** int(math.log10(num))
                msd = num // emax
                yield msd
                num -= msd * emax
        return sum(not int(num % digit) for digit in digit_iter(num))
