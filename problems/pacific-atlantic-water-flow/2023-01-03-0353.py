# Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Accepted 2023-01-03 03:53 UTC · Python · 828 ms · 15.6 MB

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def dfs(coord: tuple[int, int], visited: set[tuple[int, int]]) -> None:
            r, c = coord
            if (r, c) in visited:
                return
            visited.add((r, c))
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and (i, j) not in visited and heights[i][j] >= heights[r][c]:
                    dfs((i, j), visited)

        pacific, atlantic = set(), set()
        for i in range(m):
            dfs((i, 0), pacific)
            dfs((i, n - 1), atlantic)
        for j in range(n - 1):
            dfs((0, j + 1), pacific)
            dfs((m - 1, j), atlantic)
        return pacific.intersection(atlantic)
