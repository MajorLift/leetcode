# Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Accepted 2023-01-28 18:35 UTC · Python · 65 ms · 14 MB

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        source, target = (0, 0), (m - 1, n - 1)

        def dist_remaining(r, c):
            return sum(target) - sum((r, c))
      
        dist = [[(+math.inf, +math.inf) for _ in range(n)] for _ in range(m)]
        dist[0][0] = (0, 0)
        pq = [(0, 0, source)]
        while pq:
            steps, removals, (r, c) = heappop(pq)
            if (r, c) == target:
                break
            if k - removals >= steps + dist_remaining(r, c):
                return steps + dist_remaining(r, c)

            for i, j in (r, c - 1), (r + 1, c), (r, c + 1), (r - 1, c):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                min_state_steps, min_state_removals = dist[i][j]
                if (steps + 1 < min_state_steps or removals + grid[i][j] < min_state_removals) \
                    and removals + grid[i][j] <= k:
                    dist[i][j] = (steps + 1, removals + grid[i][j])
                    heappush(pq, (steps + 1, removals + grid[i][j], (i, j)))

        return dist[-1][-1][0] if dist[-1][-1][0] < +math.inf else -1
