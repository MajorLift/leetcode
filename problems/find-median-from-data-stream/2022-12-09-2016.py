# Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/
# Accepted 2022-12-09 20:16 UTC · Python · 1395 ms · 35.6 MB

class MedianFinder:

    def __init__(self):
        self.maxheap, self.minheap = [], []

    def addNum(self, num: int) -> None:
        if len(self.minheap) > len(self.maxheap):
            move = heapq.heappushpop(self.minheap, num)
            heapq.heappush(self.maxheap, -move)
        else:
            move = heapq.heappushpop(self.maxheap, -num)
            heapq.heappush(self.minheap, -move)

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
