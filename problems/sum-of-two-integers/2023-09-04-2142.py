# Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/
# Accepted 2023-09-04 21:42 UTC · Python · 32 ms · 16.4 MB

class Solution:
    def getSum(self, a: int, b: int) -> int:

        def to_binary_string(x: int) -> str:
            output = bin(x)[2:].rjust(32, '0')
            return output if x >= 0 else twos_complement(output)

        def twos_complement(s: str) -> str:
            i = len(s) - 1
            while i >= 0 and s[i] == '0':
                i -= 1
            return s if i == -1 else ''.join(['0' if e == '1' else '1' for e in s[:i]] + [s[i:]])

        def full_adder(x, y, carry_in):
            sum_, carry_out = x ^ y ^ carry_in, (x & y) ^ (carry_in & (x ^ y))
            return sum_, carry_out

        def carry_save_adder(a, b):
            output = sum_ = carry = 0
            for i in range(31, -1, -1):
                x, y = map(int, (a[i], b[i]))
                sum_, carry = full_adder(x, y, carry)
                output ^= sum_ << (31 - i)
            return output

        x, y = map(to_binary_string, (a, b))
        res = carry_save_adder(x, y)
        return res if not res & (1 << 31) else -1 * int(twos_complement(to_binary_string(res)), 2)
