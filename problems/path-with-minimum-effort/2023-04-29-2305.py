# Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/
# Accepted 2023-04-29 23:05 UTC · Python · 939 ms · 17.7 MB

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = map(len, (heights, heights[0]))
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dist = [[+inf] * n for _ in range(m)]
        dist[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            _, r, c = heappop(pq)
            if (r, c) == (m - 1, n - 1):
                break
            for i, j in (map(sum, zip(d, (r, c))) for d in DIRECTIONS):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                new_effort = max(dist[r][c], abs(heights[i][j] - heights[r][c]))
                if dist[i][j] > new_effort:
                    dist[i][j] = new_effort
                    heappush(pq, (dist[i][j], i, j))
        return dist[-1][-1]
