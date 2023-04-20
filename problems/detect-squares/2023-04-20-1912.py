# Detect Squares
# https://leetcode.com/problems/detect-squares/
# Accepted 2023-04-20 19:12 UTC · Python · 333 ms · 15.9 MB

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        cnt = 0
        x0, y0 = point
        for x, y in self.points:
            if abs(x - x0) == abs(y - y0) > 0 \
                and (x, y0) in self.points \
                and (x0, y) in self.points:
                cnt += self.points[(x, y)] * self.points[(x0, y)] * self.points[(x, y0)]
        return cnt


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
