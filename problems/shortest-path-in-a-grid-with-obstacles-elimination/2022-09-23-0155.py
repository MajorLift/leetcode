# Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Accepted 2022-09-23 01:55 UTC · Python · 132 ms · 15.3 MB

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        def manhattan_dist(i, j):
            return (m - 1 - i) + (n - 1 -j)
        
        curr, steps, rem_elims, estimation = (0, 0), 0, k, manhattan_dist(0, 0)
        pq = [(estimation, steps, rem_elims, curr)]
        seen = set([(curr, rem_elims)])
        
        while pq:
            estimation, steps, rem_elims, (i, j) = heapq.heappop(pq)
            if estimation - steps <= rem_elims:
                return estimation
            for row, col in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if (0 <= row < m) and (0 <= col < n):
                    new_elims = rem_elims - grid[row][col]
                    if new_elims >= 0 and ((row, col), new_elims) not in seen:
                        seen.add(((row, col), new_elims))
                        new_steps = steps + 1
                        heapq.heappush(pq, (manhattan_dist(row, col) + new_steps, new_steps, new_elims, (row, col)))
        return -1
