# Design Most Recently Used Queue
# https://leetcode.com/problems/design-most-recently-used-queue/
# Accepted 2023-05-02 22:39 UTC · Python · 162 ms · 17.6 MB

class MRUQueue:

    def __init__(self, n: int):
        self.clock = 0
        self.queue = [(0, i) for i in range(1, n + 1)]

    def fetch(self, k: int) -> int:
        self.clock += 1
        self.queue.append((self.clock, self.queue.pop(k - 1)[1]))
        return self.queue[-1][1]


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
