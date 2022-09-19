# Max Area of Island
# https://leetcode.com/problems/max-area-of-island/
# Accepted 2022-09-19 03:54 UTC · Python · 343 ms · 14.4 MB

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    curr_area = 0
                    stack = [(i, j)]
                    visited.add((i, j))
                    while stack:
                        r, c = stack.pop()
                        curr_area += 1
                        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                            if 0 <= nr < m and 0 <= nc < n \
                            and grid[nr][nc] == 1 \
                            and (nr, nc) not in visited:
                                stack.append((nr, nc))
                                visited.add((nr, nc))
                    max_area = max(max_area, curr_area)
        return max_area
