# Range Module
# https://leetcode.com/problems/range-module/
# Accepted 2023-05-02 02:17 UTC · Python · 357 ms · 20.6 MB

class RangeModule:

    def __init__(self):
        self.intervals = []        

    def addRange(self, left: int, right: int) -> None:
        l, r = bisect_left(self.intervals, left), bisect_right(self.intervals, right)
        self.intervals[l:r] = ([left] if l % 2 == 0 else []) \
            + ([right] if r % 2 == 0 else [])

    def queryRange(self, left: int, right: int) -> bool:
        l, r = bisect_right(self.intervals, left), bisect_left(self.intervals, right)
        return l % 2 == 1 and l == r

    def removeRange(self, left: int, right: int) -> None:
        l, r = bisect_left(self.intervals, left), bisect_right(self.intervals, right)
        self.intervals[l:r] = ([left] if l % 2 == 1 else []) \
            + ([right] if r % 2 == 1 else [])


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
