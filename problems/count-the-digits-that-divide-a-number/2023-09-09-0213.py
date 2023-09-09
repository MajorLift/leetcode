# Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/
# Accepted 2023-09-09 02:13 UTC · Python · 39 ms · 16.2 MB

class Solution:
    def countDigits(self, num: int) -> int:
        def digit_iter(num: int):
            while num:
                pos = 10 ** int(math.log10(num))
                msd = num // pos
                yield msd
                num -= msd * pos
        return sum(not num % digit for digit in digit_iter(num))
