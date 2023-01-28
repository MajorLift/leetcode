# Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Accepted 2023-01-28 23:11 UTC · Python · 58 ms · 14.2 MB

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
            manhattan_dist = sum(target) - sum((r, c))
            if k - removals >= manhattan_dist:
                heappush(pq, (steps + manhattan_dist, removals + manhattan_dist, target))
                min_steps_target, min_removals_target = dist[-1][-1]
                if steps + manhattan_dist < min_steps_target:
                    dist[-1][-1] = (steps + manhattan_dist, removals + manhattan_dist)
                continue

            for i, j in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                min_steps_next, min_removals_next = dist[i][j]
                steps_next, removals_next = steps + 1, removals + grid[i][j]

                if (steps_next < min_steps_next
                    or (min_steps_next <= steps_next < +math.inf 
                        and removals_next < min_removals_next)):
                    dist[i][j] = (steps_next, removals_next)
                    if removals_next <= k:
                        heappush(pq, (steps_next, removals_next, (i, j)))

        min_steps_to_target = dist[-1][-1][0]
        return min_steps_to_target if min_steps_to_target < +math.inf else -1
