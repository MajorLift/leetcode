# Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/
# Accepted 2023-04-29 22:27 UTC · Python · 3033 ms · 29.1 MB

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = map(len, (heights, heights[0]))
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        
        def dfs(r, c, effort):
            if (r, c) == (m - 1, n - 1):
                return True
            visited.add((r, c))
            flag = False
            for i, j in (map(sum, zip((r, c), d)) for d in DIRECTIONS):
                if not (0 <= i < m and 0 <= j < n) \
                    or (i, j) in visited \
                    or abs(heights[i][j] - heights[r][c]) > effort:
                    continue
                flag = flag or dfs(i, j, effort)
            return flag

        lo, hi = 0, 10 ** 6
        while lo < hi:
            mid = (lo + hi) // 2
            visited = set()
            if dfs(0, 0, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
