# Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Accepted 2023-05-01 05:23 UTC · Python · 93 ms · 17.6 MB

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = map(len, (grid, grid[0]))
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        SRC, DST = (0, 0), (m - 1, n - 1)
        self.total = sum(DST)

        pq = [(self.manhattan(*SRC), 0, 0, SRC)]
        visited = set([(*SRC, 0)])
        while pq:
            heuristic, removals, steps, (r, c) = heappop(pq)
            if removals + self.manhattan(r, c) <= k:
                return heuristic
            if (r, c) == DST:
                return heuristic
            for i, j in (map(sum, zip((r, c), d)) for d in DIRECTIONS):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                removals_uv = removals + grid[i][j]
                if removals_uv <= k and (i, j, removals_uv) not in visited:
                    visited.add((i, j, removals_uv))
                    heappush(pq, (
                        self.manhattan(i, j) + steps + 1, 
                        removals_uv, 
                        steps + 1, 
                        (i, j)))

        return -1            

    def manhattan(self, x, y):
        return self.total - sum((x, y))
