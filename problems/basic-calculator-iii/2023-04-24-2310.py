# Basic Calculator III
# https://leetcode.com/problems/basic-calculator-iii/
# Accepted 2023-04-24 23:10 UTC · Python · 56 ms · 14 MB

class Solution:
    def calculate(self, s) -> int:
        self.OPERATORS = set(["+", "-", "*", "/"])
        self.PARENS = set(["(", ")"])
        self.TOKENS = self.OPERATORS | self.PARENS

        exp = self.parse(s)
        paren_stack = []
        r = 0
        while r < len(exp):
            if exp[r] == "(":
                paren_stack.append(r)
            elif exp[r] == ")":
                l = paren_stack.pop()
                exp[l:r+1] = [self.eval_expression(exp[l+1:r])]
                r = l
            r += 1
        print(exp)
        return self.eval_expression(exp)

    def parse(self, exp):
        output = []
        for char in exp:
            if char not in self.TOKENS:
                if not output or output[-1] in self.TOKENS:
                    output.append(char)
                elif output[-1] not in self.TOKENS:
                    output[-1] += char
            else:
                if output and output[-1] not in self.TOKENS:
                    output[-1] = int(output[-1])
                output.append(char)
        if output[-1] not in self.TOKENS:
            output[-1] = int(output[-1])
        return output
        
    def eval_expression(self, exp):
        op_stack, num_stack = deque(), deque()
        for elem in exp:
            if elem in self.OPERATORS:
                op_stack.append(elem)
            else:
                if op_stack and op_stack[-1] in ("*", "/"):
                    op, num = op_stack.pop(), num_stack.pop()
                    if op == "*":
                        num_stack.append(num * elem)
                    if op == "/":
                        num_stack.append(num // elem if num * elem >= 0 else num // elem + 1)
                else:
                    num_stack.append(elem)
        
        while len(num_stack) > 1:
            x, y = num_stack.popleft(), num_stack.popleft()
            op = op_stack.popleft()
            if op == "+":
                num_stack.appendleft(x + y)
            if op == "-":
                num_stack.appendleft(x - y)

        return num_stack.pop()
