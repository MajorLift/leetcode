# Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/
# Accepted 2023-09-08 16:44 UTC · Python · 38 ms · 16.3 MB

class Solution:
    def countDigits(self, num: int) -> int:
        ans, tmp = 0, num
        while tmp:
            if not num % (tmp % 10):
                ans += 1
            tmp //= 10
        return ans
