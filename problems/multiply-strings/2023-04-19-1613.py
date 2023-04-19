# Multiply Strings
# https://leetcode.com/problems/multiply-strings/
# Accepted 2023-04-19 16:13 UTC · Python · 345 ms · 14.2 MB

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        shorter, longer = sorted((num1, num2), key=len)
        acc = '0'
        for i, digit in enumerate(reversed(shorter)):
            acc = self.add(acc, self.padRight(
                self.multiplyByDigit(longer, digit), '0', i
            ))
        return acc

    def multiplyByDigit(self, multiplicand: str, multiplier: str) -> str:
        if multiplier == '0':
            return '0'
        output = deque()
        multiplier = self.aToI(multiplier)
        carry = 0
        for digit in map(self.aToI, reversed(multiplicand)):
            mul = digit * multiplier + carry
            carry = mul // 10
            output.appendleft(mul % 10)
        if carry > 0:
            output.appendleft(carry)
        return ''.join(map(str, output))

    def padLeft(self, n: str, digit: str, k: int) -> str:
        return ''.join([digit] * k + list(n))

    def padRight(self, n: str, digit: str, k: int) -> str:
        return ''.join(list(n) + [digit] * k)
    
    def add(self, num1: str, num2: str) -> str:
        shorter, longer = sorted((num1, num2), key=len)
        shorter = self.padLeft(shorter, '0', len(longer) - len(shorter))
        output = deque()
        carry = 0
        for a, b in zip(*map(reversed, (shorter, longer))):
            sum_ = sum(map(self.aToI, (a, b))) + carry
            carry = sum_ // 10
            output.appendleft(sum_ % 10)
        if carry == 1:            
            output.appendleft('1')
        return ''.join(map(str, output))

    def aToI(self, digit: str) -> int:
        return ord(digit) - ord('0')
