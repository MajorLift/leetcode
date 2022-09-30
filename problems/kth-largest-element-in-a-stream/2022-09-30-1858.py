# Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Accepted 2022-09-30 18:58 UTC · Python · 202 ms · 18.2 MB

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.maxheap = [], []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
                heappush(self.minheap, val)
        else:
            if self.minheap[0] >= val:
                heappush(self.maxheap, -val)
            else:
                tmp = heappop(self.minheap)
                heappush(self.maxheap, -tmp)
                heappush(self.minheap, val)
        return self.minheap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
