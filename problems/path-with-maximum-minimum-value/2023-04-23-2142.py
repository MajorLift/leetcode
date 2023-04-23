# Path With Maximum Minimum Value
# https://leetcode.com/problems/path-with-maximum-minimum-value/
# Accepted 2023-04-23 21:42 UTC · Python · 8905 ms · 16.7 MB

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.DIRECTIONS = ((1, 0), (0, -1), (-1, 0), (0, 1))
        
        candidates = list(filter(
            lambda x: x <= min(grid[0][0], grid[-1][-1]), 
            sorted(set(grid[i][j] for i, j in product(range(self.m), range(self.n))))))
        lo, hi = 0, len(candidates) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.has_path(candidates[mid]):
                lo = mid
            else:
                hi = mid - 1
        return candidates[lo]

    def has_path(self, score):
        queue, visited = deque([(0, 0)]), set([(0, 0)])
        while queue:
            x, y = queue.popleft()
            if (x, y) == (self.m - 1, self.n - 1):
                return True
            for i, j in (map(sum, zip((x, y), d)) for d in self.DIRECTIONS):
                if not (0 <= i < self.m and 0 <= j < self.n) \
                    or (i, j) in visited \
                    or self.grid[i][j] < score:
                    continue
                queue.append((i, j))
                visited.add((i, j))
        return False
