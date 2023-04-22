# Minimum Moves to Move a Box to Their Target Location
# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/
# Accepted 2023-04-22 16:35 UTC · Python · 899 ms · 22 MB

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        self.grid, self.m, self.n = grid, len(grid), len(grid[0])
        self.DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        start_player, start_box, (self.xt, self.yt) = map(self.findCellType, ('S', 'B', 'T'))
        pq = [(self.heuristic(*start_box), 0, start_box, start_player)]
        visited = set()
        while pq:
            _, moves, box, player = heappop(pq)
            if (box, player) in visited:
                continue
            visited.add((box, player))
            if box == (self.xt, self.yt):
                return moves
            for d in self.DIRECTIONS:
                next_player = tuple(map(sum, zip(player, d)))
                if not self.valid(*next_player):
                    continue
                if next_player == box:
                    next_box = tuple(map(sum, zip(box, d)))
                    if not self.valid(*next_box):
                        continue
                    heappush(pq, (self.heuristic(*next_box) + moves + 1, moves + 1, next_box, next_player))
                else:
                    heappush(pq, (self.heuristic(*box) + moves, moves, box, next_player))
        return -1
    
    def heuristic(self, x, y):
        return abs(self.xt - x) + abs(self.yt - y)
    
    def valid(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n \
            and self.grid[x][y] != '#'
        
    def findCellType(self, cell_type):
        for i, j in product(range(self.m), range(self.n)):
            if self.grid[i][j] == cell_type:
                return (i, j)
