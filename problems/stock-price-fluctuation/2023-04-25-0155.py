# Stock Price Fluctuation
# https://leetcode.com/problems/stock-price-fluctuation/
# Accepted 2023-04-25 01:55 UTC · Python · 760 ms · 61.1 MB

class StockPrice:

    def __init__(self):
        self.records = dict()
        self.maxheap, self.minheap = [], []
        self.latest = -inf

    def update(self, timestamp: int, price: int) -> None:
        self.records[timestamp] = price
        heappush(self.maxheap, (-price, timestamp))
        heappush(self.minheap, (price, timestamp))
        self.latest = max(self.latest, timestamp)

    def current(self) -> int:
        return self.records[self.latest]

    def maximum(self) -> int:
        price, time = self.maxheap[0]
        while -price != self.records[time]:
            heappop(self.maxheap)
            price, time = self.maxheap[0]
        return -self.maxheap[0][0]

    def minimum(self) -> int:
        price, time = self.minheap[0]
        while price != self.records[time]:
            heappop(self.minheap)
            price, time = self.minheap[0]
        return self.minheap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
