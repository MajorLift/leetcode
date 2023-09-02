# Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/
# Accepted 2023-09-02 20:30 UTC · Python · 36 ms · 16.3 MB

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 33) - 1 
        while b ^ 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= (mask >> 1) else ~(a ^ mask)
