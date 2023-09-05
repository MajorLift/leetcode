# Smallest Even Multiple
# https://leetcode.com/problems/smallest-even-multiple/
# Accepted 2023-09-05 04:30 UTC · Python · 33 ms · 16.2 MB

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n << 1 if n & 1 else n
