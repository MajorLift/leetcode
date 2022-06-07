# Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/
# Accepted 2022-06-07 03:17 UTC · Python · 9003 ms · 35.9 MB

class MedianFinder:
    
    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        top = -heapq.heappushpop(self.lo, -num)
        heapq.heappush(self.hi, top)
        if len(self.hi) > len(self.lo):
            bottom = -heapq.heappop(self.hi)
            heapq.heappush(self.lo, bottom)

    def findMedian(self) -> float:
        return -heapq.nsmallest(1, self.lo).pop() if len(self.lo) > len(self.hi) \
            else (-heapq.nsmallest(1, self.lo).pop() + heapq.nsmallest(1, self.hi).pop()) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
