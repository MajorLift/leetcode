# Pow(x, n)
# https://leetcode.com/problems/powx-n/
# Accepted 2023-04-17 22:47 UTC · Python · 37 ms · 14 MB

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.power(x, n) if n >= 0 else self.power(1 / x, -n)

    @cache
    def power(self, x, n):
        if n == 0: return 1
        if n == 1: return x
        sqrt = self.power(x, n // 2)
        return sqrt * sqrt * self.power(x, n % 2)
