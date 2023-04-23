# Path With Maximum Minimum Value
# https://leetcode.com/problems/path-with-maximum-minimum-value/
# Accepted 2023-04-23 19:41 UTC · Python · 6775 ms · 32.4 MB

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.DIRECTIONS = ((1, 0), (0, -1), (-1, 0), (0, 1))
        
        sup = min(grid[0][0], grid[-1][-1])
        vals = sorted(set(grid[i][j] for i, j in product(range(self.m), range(self.n))))
        candidates = vals[:bisect_right(vals, sup)]
        lo, hi = 0, len(candidates) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.has_path(candidates[mid]):
                lo = mid
            else:
                hi = mid - 1
        return candidates[lo]

    def has_path(self, score):
        visited = set()
        def dfs(x, y):
            if (x, y) == (self.m - 1, self.n - 1):
                return True
            visited.add((x, y))
            for i, j in (map(sum, zip((x, y), d)) for d in self.DIRECTIONS):
                if not (0 <= i < self.m and 0 <= j < self.n) \
                    or self.grid[i][j] < score \
                    or (i, j) in visited:
                    continue
                if dfs(i, j):
                    return True
            return False
        return dfs(0, 0)
