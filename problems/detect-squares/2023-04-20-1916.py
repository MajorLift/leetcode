# Detect Squares
# https://leetcode.com/problems/detect-squares/
# Accepted 2023-04-20 19:16 UTC · Python · 378 ms · 16.2 MB

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.points_x, self.points_y = defaultdict(list), defaultdict(list)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.points_x[x].append(y)
        self.points_y[y].append(x)

    def count(self, point: List[int]) -> int:
        x0, y0 = point
        xdist, ydist = defaultdict(set), defaultdict(set)
        for x in self.points_y[y0]:
            xdist[abs(x - x0)].add(x)
        for y in self.points_x[x0]:
            ydist[abs(y - y0)].add(y)
        candidates = xdist.keys() & ydist.keys() - {0}
        ans = 0
        for d in candidates:
            for x, y in product(xdist[d], ydist[d]):
                ans += self.points[(x, y)] * self.points[(x, y0)] * self.points[(x0, y)]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
