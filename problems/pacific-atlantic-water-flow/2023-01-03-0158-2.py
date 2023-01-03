# Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Accepted 2023-01-03 01:58 UTC · Python · 437 ms · 17.7 MB

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        adj = [[[] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                for r, c in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= r < m and 0 <= c < n and heights[i][j] >= heights[r][c]:
                        adj[r][c].append((i, j))

        def dfs(stack: list[tuple[int, int]], output: set[tuple[int, int]]) -> set[tuple[int, int]]:
            while stack:
                i, j = stack.pop()
                output.add((i, j))
                for u in adj[i][j]:
                    if u not in output:
                        stack.append(u)
            return output

        pacific = dfs([(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)], set())
        atlantic = dfs([(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n - 1)], set())
        return [[i, j] for i, j in pacific.intersection(atlantic)]
