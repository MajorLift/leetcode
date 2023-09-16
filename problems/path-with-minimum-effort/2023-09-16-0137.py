# Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/
# Accepted 2023-09-16 01:37 UTC · Python · 4400 ms (5.04%) · 18.5 MB (47.28%)

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = map(len, (heights, heights[0]))
        SRC, DST = (0, 0), (m - 1, n - 1)
        DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(effort):
            stack, visited = [SRC], set([SRC])
            while stack:
                r, c = stack.pop()
                if (r, c) == DST:
                    return True
                for i, j in (map(sum, zip((r, c), d)) for d in DIRS):
                    if not (0 <= i < m and 0 <= j < n) or (i, j) in visited: continue
                    if abs(heights[r][c] - heights[i][j]) <= effort:
                        visited.add((i, j))
                        stack.append((i, j))
            return False

        return bisect_left(a=range(10 ** 6), x=True, key=dfs)
