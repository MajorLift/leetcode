# Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/
# Accepted 2023-09-02 21:18 UTC · Python · 40 ms · 16.4 MB

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 33) - 1 
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= (mask >> 1) else ~(a ^ mask)
