# Minimum Moves to Move a Box to Their Target Location
# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/
# Accepted 2023-04-22 16:06 UTC · Python · 709 ms · 14.2 MB

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        self.grid, self.m, self.n = grid, len(grid), len(grid[0])
        self.DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        (xs, ys), (xb, yb), (xt, yt) = map(self.findCellType, ('S', 'B', 'T'))

        visited = set([((xb, yb), (xs, ys))])
        pq = [(0, (xb, yb), (xs, ys))]
        while pq:
            moves, (rb, cb), (rs, cs) = heappop(pq)
            if (rb, cb) == (xt, yt):
                return moves
            for d in self.DIRECTIONS:
                ib, jb = map(sum, zip((rb, cb), d))
                is_, js = map(sum, zip((rb, cb), map(operator.neg, d)))
                if not self.valid(ib, jb) \
                    or not self.valid(is_, js) \
                    or not self.traversable((rs, cs), (is_, js), (rb, cb)) \
                    or ((ib, jb), (is_, js)) in visited:
                    continue
                heappush(pq, (moves + 1, (ib, jb), (is_, js)))
                visited.add(((ib, jb), (is_, js)))
        return -1
    
    def manhattanDist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def valid(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n \
            and self.grid[x][y] != '#'

    def traversable(self, src, dst, box):
        queue, visited = deque([src]), set()
        while queue:
            curr = queue.popleft()
            if curr == dst:
                return True
            for i, j in (map(sum, zip(d, curr)) for d in self.DIRECTIONS):
                if self.valid(i, j) \
                    and (i, j) != box \
                    and (i, j) not in visited:
                    visited.add((i, j))
                    queue.append((i, j))
        return False
        
    def findCellType(self, cell_type):
        for i, j in product(range(self.m), range(self.n)):
            if self.grid[i][j] == cell_type:
                return (i, j)
