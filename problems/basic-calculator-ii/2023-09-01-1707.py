# Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/
# Accepted 2023-09-01 17:07 UTC · Python · 208 ms · 26 MB

class Solution:
    def calculate(self, s: str) -> int:
        arr = self.parse([char for char in s if char != " "])
        # print(arr)
        num_stack, op_stack = self.muldiv(arr)
        # print(num_stack, op_stack)
        res = self.addsub(num_stack, op_stack)
        # print(res)
        return res

    def parse(self, arr):
        output = []
        for char in arr:
            if char in {"+", "-", "*", "/"}:
                output.append(char)
            elif char.isnumeric():
                if output and output[-1].isnumeric():
                    output.append(output.pop() + char)
                else:
                    output.append(char)
        return [int(e) if i % 2 == 0 else e for i,e in enumerate(output)]

    def muldiv(self, arr):
        num_stack, op_stack = deque(), deque()
        for i,e in enumerate(arr):
            if i % 2 == 0:
                if op_stack and op_stack[-1] == "*":
                    num_stack.append(num_stack.pop() * e)
                    op_stack.pop()
                elif op_stack and op_stack[-1] == "/":
                    num_stack.append(int(num_stack.pop() / e))
                    op_stack.pop()
                else:
                    num_stack.append(e)
            else:
                op_stack.append(e)
        return num_stack, op_stack

    def addsub(self, num_stack, op_stack):
        while len(num_stack) > 1:
            x, y, op = num_stack.popleft(), num_stack.popleft(), op_stack.popleft()
            if op == "+":
                num_stack.appendleft(x + y)
            if op == "-":
                num_stack.appendleft(x - y)
        return int(num_stack.pop())
