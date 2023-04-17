# Plus One
# https://leetcode.com/problems/plus-one/
# Accepted 2023-04-17 21:10 UTC · Python · 33 ms · 13.8 MB

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last, rest = digits[-1], digits[:-1]
        if last < 9:
            return rest + [last + 1]
        elif not rest:
            return [1, 0]
        else:
            return self.plusOne(rest) + [0]
