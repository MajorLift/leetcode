# Pow(x, n)
# https://leetcode.com/problems/powx-n/
# Accepted 2023-02-28 08:14 UTC · Python · 23 ms · 13.9 MB

class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def power(x, n):
            if n == 0: return 1.0
            sqrt = power(x, n // 2)
            if n % 2 == 0:
                return sqrt * sqrt
            return sqrt * sqrt * x

        return power(x, n) if n >= 0 else power(1 / x, -n)
