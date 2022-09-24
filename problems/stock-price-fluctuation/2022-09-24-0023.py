# Stock Price Fluctuation
# https://leetcode.com/problems/stock-price-fluctuation/
# Accepted 2022-09-24 00:23 UTC · Python · 781 ms · 60.9 MB

class StockPrice:

    def __init__(self):
        self.latest_time = 0
        self.timepricemap = {} 
        self.minheap = []
        self.maxheap = []

    def update(self, timestamp: int, price: int) -> None:
        self.timepricemap[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)
        heappush(self.minheap, (price, timestamp))
        heappush(self.maxheap, (-price, timestamp))

    def current(self) -> int:
        return self.timepricemap[self.latest_time]

    def maximum(self) -> int:
        price, timestamp = self.maxheap[0]
        while -price != self.timepricemap[timestamp]:
            heappop(self.maxheap)
            price, timestamp = self.maxheap[0]
        return -price

    def minimum(self) -> int:
        price, timestamp = self.minheap[0]
        while price != self.timepricemap[timestamp]:
            heappop(self.minheap)
            price, timestamp = self.minheap[0]
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
