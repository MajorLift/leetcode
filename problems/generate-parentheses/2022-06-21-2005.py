# Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# Accepted 2022-06-21 20:05 UTC · Python · 48 ms · 14.3 MB

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def recurse(comb, numOpen, numClose):
            nonlocal output
            if numOpen < n:
                recurse(comb + "(", numOpen + 1, numClose)
                if numClose < numOpen:
                    recurse(comb + ")", numOpen, numClose + 1)
            elif numClose < n:
                recurse(comb + ")", numOpen, numClose + 1)
            else:
                output.append(comb)
        recurse("(", 1, 0)
        return output
