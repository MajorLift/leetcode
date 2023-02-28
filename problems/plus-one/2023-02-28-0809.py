# Plus One
# https://leetcode.com/problems/plus-one/
# Accepted 2023-02-28 08:09 UTC · Python · 30 ms · 13.8 MB

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            curr = carry + digits[i]
            if i == len(digits) - 1:
                curr += 1
            carry = curr // 10
            digits[i] = curr % 10
        return [1] + digits if carry > 0 else digits
