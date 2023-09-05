# Smallest Even Multiple
# https://leetcode.com/problems/smallest-even-multiple/
# Accepted 2023-09-05 04:31 UTC · Python · 37 ms · 16.3 MB

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n << (n & 1)
