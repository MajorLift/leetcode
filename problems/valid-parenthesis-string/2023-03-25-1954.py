# Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/
# Accepted 2023-03-25 19:54 UTC · Python · 40 ms · 13.9 MB

class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin = openMax = 0
        for char in s:
            openMin += 1 if char == "(" else -1
            if openMin < 0:
                openMin = 0
            openMax += 1 if char in ("(", "*") else -1
            if openMax < 0:
                return False
        return openMin == 0
