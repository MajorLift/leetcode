# Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/
# Accepted 2023-09-05 02:49 UTC · Python · 34 ms · 16.3 MB

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = (1 << 32) - 1

        def full_adder(x: int, y: int, carry_in: int) -> tuple[int, int]:
            sum_, carry_out = x ^ y ^ carry_in, (x & y) ^ (carry_in & (x ^ y))
            return sum_, carry_out

        def ripple_carry_adder(a: int, b: int) -> int:
            output = carry = 0
            counter = 1
            while a or b or carry:
                sum_, carry = full_adder(a & 1, b & 1, carry)
                output ^= sum_ << int(math.log2(counter))
                a >>= 1
                b >>= 1
                counter <<= 1
            return output

        res = ripple_carry_adder(a & mask, b & mask) & mask
        return res if not res & (1 << 31) else res ^ ~mask
