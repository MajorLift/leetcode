# Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water/
# Accepted 2023-01-25 07:24 UTC · Python · 182 ms · 14.8 MB

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def dfs(t):
            visited = set([(0, 0)])
            stack = [(0, 0)]
            while stack:
                i, j = stack.pop()
                if i == j == n - 1:
                    return True
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n and (x, y) not in visited and grid[x][y] <= t:
                        stack.append((x, y))
                        visited.add((x, y))
            return False
        return bisect_left([i for i in range(0, n * n)], True, lo=grid[0][0], key=lambda x: dfs(x))
