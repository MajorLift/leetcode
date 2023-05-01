# Path With Maximum Minimum Value
# https://leetcode.com/problems/path-with-maximum-minimum-value/
# Accepted 2023-05-01 23:10 UTC · Python · 1763 ms · 34.4 MB

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m, self.n = map(len, (grid, grid[0]))
        self.DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

        candidates = sorted(filter(
            lambda x: x <= min(grid[0][0], grid[-1][-1]),
            set([e for row in grid for e in row])))
        lo, hi = 0, len(candidates) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.pathExists(candidates[mid]):
                lo = mid
            else:
                hi = mid - 1
        return candidates[lo]

    def pathExists(self, score):
        visited = set()
        def dfs(r, c):
            if (r, c) == (self.m - 1, self.n - 1):
                return True
            for i, j in (map(sum, zip((r, c), d)) for d in self.DIRECTIONS):
                if not (0 <= i < self.m and 0 <= j < self.n) \
                    or self.grid[i][j] < score \
                    or (i, j) in visited:
                    continue
                visited.add((i, j))
                if dfs(i, j):
                    return True
            return False
        return dfs(0, 0)
