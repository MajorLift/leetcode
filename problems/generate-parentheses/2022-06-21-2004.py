# Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# Accepted 2022-06-21 20:04 UTC · Python · 41 ms · 14.1 MB

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(comb, numOpen, numClose):
            nonlocal output
            if numOpen < n:
                backtrack(comb + "(", numOpen + 1, numClose)
                if numClose < numOpen:
                    backtrack(comb + ")", numOpen, numClose + 1)
            elif numClose < n:
                backtrack(comb + ")", numOpen, numClose + 1)
            else:
                output.append(comb)
        backtrack("(", 1, 0)
        return output
