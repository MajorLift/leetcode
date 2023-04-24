# Range Module
# https://leetcode.com/problems/range-module/
# Accepted 2023-04-24 21:34 UTC · Python · 383 ms · 18.6 MB

class RangeModule:

    def __init__(self):
        self.arr = []        

    def addRange(self, left: int, right: int) -> None:
        start, end = bisect_left(self.arr, left), bisect_right(self.arr, right)
        self.arr[start:end] = ([left], [])[start % 2] + ([right], [])[end % 2]

    def queryRange(self, left: int, right: int) -> bool:
        start, end = bisect_right(self.arr, left), bisect_left(self.arr, right)
        return start % 2 and start == end

    def removeRange(self, left: int, right: int) -> None:
        start, end = bisect_left(self.arr, left), bisect_right(self.arr, right)
        self.arr[start:end] = ([left], [])[1 - start % 2] + ([right], [])[1 - end % 2]

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
