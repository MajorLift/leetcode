# Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Accepted 2022-09-24 00:44 UTC · Python · 76 ms · 14.4 MB

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ("+", "-", "*", '/')
        tokens = [int(x) if x not in operators else x for x in tokens]
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                b, a = stack.pop(), stack.pop()
                curr = 0
                if token == "+":
                    curr = a + b
                if token == "-":
                    curr = a - b
                if token == "*":
                    curr = a * b
                if token == "/":
                    curr = int(a / b)
                stack.append(curr)
        return stack.pop()
