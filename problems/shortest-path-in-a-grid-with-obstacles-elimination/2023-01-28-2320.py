# Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Accepted 2023-01-28 23:20 UTC · Python · 62 ms · 14 MB

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        source, target = (0, 0), (m - 1, n - 1)
        dist = [[(+math.inf, +math.inf) for _ in range(n)] for _ in range(m)]
        dist[0][0] = (0, 0)
        pq = [(0, 0, source)]
        while pq:
            steps, removals, (r, c) = heappop(pq)
            if (r, c) == target:
                break

            manhattan_dist_to_target = sum(target) - sum((r, c))
            if k - removals >= manhattan_dist_to_target:
                min_steps_target, min_removals_target = dist[-1][-1]
                if steps + manhattan_dist_to_target < min_steps_target:
                    dist[-1][-1] = (steps + manhattan_dist_to_target, removals + manhattan_dist_to_target)
                heappush(pq, (steps + manhattan_dist_to_target, removals + manhattan_dist_to_target, target))
                continue

            for i, j in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                min_steps_next, min_removals_next = dist[i][j]
                if (steps + 1 < min_steps_next
                    or (min_steps_next <= steps + 1 < +math.inf 
                        and removals + grid[i][j] < min_removals_next)):
                    dist[i][j] = (steps + 1, removals + grid[i][j])
                    if removals + grid[i][j] <= k:
                        heappush(pq, (steps + 1, removals + grid[i][j], (i, j)))

        min_steps_to_target = dist[-1][-1][0]
        return min_steps_to_target if min_steps_to_target < +math.inf else -1
