# Plus One
# https://leetcode.com/problems/plus-one/
# Accepted 2023-04-17 21:16 UTC · Python · 19 ms · 13.9 MB

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = digits.pop() + 1
        if last == 10:
            return (self.plusOne(digits) if digits else [1]) + [0]
        return digits + [last]
