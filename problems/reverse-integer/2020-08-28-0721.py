# Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# Accepted 2020-08-28 07:21 UTC · Python · 24 ms · 14 MB

class Solution:
    def reverse(self, x: int) -> int:
        sgn = 0
        if x < 0:
            sgn = 1
            x = -x
        
        arr = []
        while True:
            digit = x % 10
            arr.append(digit)
            x -= digit
            if x == 0:
                break
            else:
                x /= 10
        
        result = 0
        for e in arr:
            result *= 10
            result += e
            
        if sgn == 1:
            result *= -1
            
        if result > 2**31 - 1 or result < -2**31:
            return 0
        return int(result)
