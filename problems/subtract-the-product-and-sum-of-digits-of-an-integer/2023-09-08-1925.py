# Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Accepted 2023-09-08 19:25 UTC · Python · 42 ms · 16.2 MB

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return reduce(lambda acc, curr: acc * int(curr), str(n), 1) - sum(int(e) for e in str(n))
