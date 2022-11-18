# Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Accepted 2022-11-18 03:14 UTC · Python · 142 ms · 15.3 MB

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        def manhattan_dist(i, j):
            return (m - 1 - i) + (n - 1 - j)
        
        estimation, steps, elims, cell = manhattan_dist(0, 0), 0, 0, (0, 0)
        pq = [(estimation, steps, elims, cell)]
        visited = {(cell, elims)}
        while pq:
            estimation, steps, elims, (x, y) = heapq.heappop(pq)
            if estimation - steps <= k - elims:
                return estimation
            for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= i < m and 0 <= j < n:
                    next_elims = elims + grid[i][j]
                    if next_elims <= k and ((i, j), next_elims) not in visited:
                        visited.add(((i, j), next_elims))
                        heapq.heappush(pq, (manhattan_dist(i, j) + steps + 1, steps + 1, next_elims, (i, j)))
        return -1
