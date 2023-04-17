# Plus One
# https://leetcode.com/problems/plus-one/
# Accepted 2023-04-17 21:14 UTC · Python · 42 ms · 13.9 MB

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last, rest = digits[-1], digits[:-1]
        if last == 9:
            return (self.plusOne(rest) if rest else [1]) + [0]
        return rest + [last + 1]
