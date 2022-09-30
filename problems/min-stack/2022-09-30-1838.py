# Min Stack
# https://leetcode.com/problems/min-stack/
# Accepted 2022-09-30 18:38 UTC · Python · 128 ms · 17.8 MB

class MinStack:

    def __init__(self):
        self.stack = []
        self.tracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.tracker and self.tracker[-1][0] <= val:
            self.tracker[-1][1] += 1
        else:
            self.tracker.append([val, 1])

    def pop(self) -> None:
        self.stack.pop()
        self.tracker[-1][1] -= 1
        if self.tracker[-1][1] == 0:
            self.tracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.tracker[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
