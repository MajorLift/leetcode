# My Calendar I
# https://leetcode.com/problems/my-calendar-i/
# Accepted 2023-04-25 00:13 UTC · Python · 188 ms · 14.7 MB

class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        l, r = bisect_right(self.cal, start), bisect_left(self.cal, end)
        if l == r and l % 2 == 0:
            self.cal[l:r] = [start, end]
            return True
        return False
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
