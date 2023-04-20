# Detect Squares
# https://leetcode.com/problems/detect-squares/
# Accepted 2023-04-20 19:45 UTC · Python · 345 ms · 15.9 MB

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x0, y0 = point
        return sum(
            self.points[(x, y)]
            * self.points.get((x0, y), 0)
            * self.points.get((x, y0), 0)
            for x, y in self.points
            if abs(x - x0) == abs(y - y0) > 0)
