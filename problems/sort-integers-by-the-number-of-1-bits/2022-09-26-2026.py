# Sort Integers by The Number of 1 Bits
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
# Accepted 2022-09-26 20:26 UTC · Python · 166 ms · 14.1 MB

class Solution:
    def getBitCount(self, x):
        count = 0
        while x > 0:
            if x & 1:
                count += 1
            x >>= 1
        return count
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda num: (self.getBitCount(num), num))
