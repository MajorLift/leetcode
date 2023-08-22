# Design Most Recently Used Queue
# https://leetcode.com/problems/design-most-recently-used-queue/
# Accepted 2023-08-22 20:37 UTC · Python · 207 ms · 17.9 MB

from sortedcontainers import SortedList

class MRUQueue:

    def __init__(self, n: int):
        self.clock = 0
        self.queue = SortedList((0, i) for i in range(1, n + 1))

    def fetch(self, k: int) -> int:
        self.clock += 1
        self.queue.add((self.clock, self.queue.pop(k - 1)[1]))
        return self.queue[-1][1]


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
