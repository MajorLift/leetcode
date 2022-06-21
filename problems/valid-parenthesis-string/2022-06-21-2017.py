# Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/
# Accepted 2022-06-21 20:17 UTC · Python · 46 ms · 13.8 MB

class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin = openMax = 0
        
        for c in s:
            openMin += 1 if c == '(' else -1
            if openMin < 0:
                openMin = 0
                
            openMax += 1 if c == '(' or c == '*' else -1
            if openMax < 0:
                return False
            
        return openMin == 0
