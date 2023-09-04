# Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/
# Accepted 2023-09-04 21:55 UTC · Python · 36 ms · 16.2 MB

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 33) - 1

        def full_adder(x: int, y: int, carry_in: int) -> tuple[int, int]:
            sum_, carry_out = x ^ y ^ carry_in, (x & y) ^ (carry_in & (x ^ y))
            return sum_, carry_out

        def carry_save_adder(a, b):
            output = sum_ = carry = i = 0
            while a or b or carry:
                x, y = a & (1 << 0), b & (1 << 0)
                sum_, carry = full_adder(x, y, carry)
                output ^= sum_ << i
                a >>= 1
                b >>= 1
                i += 1
            return output

        res = carry_save_adder(a & mask, b & mask) & mask
        return res if not res & (1 << 31) else ~(res ^ mask)
