# Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Accepted 2023-01-03 01:50 UTC · Python · 967 ms · 17.9 MB

from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        if m == 1 or n == 1:
            return [[i, j] for i in range(m) for j in range(n)]
        
        adj = [[[] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                for r, c in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= r < m and 0 <= c < n and heights[i][j] >= heights[r][c]:
                        adj[r][c].append((i, j))
        # print(adj)

        p_stack = [(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)]
        a_stack = [(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n - 1)]
        p_visited, a_visited = set(), set()
        pacific, atlantic = set(), set()

        while p_stack:
            i, j = p_stack.pop()
            p_visited.add((i, j))
            for u in adj[i][j]:
                if u not in p_visited:
                    p_stack.append(u)
            else:
                pacific.add((i, j))

        while a_stack:
            i, j = a_stack.pop()
            a_visited.add((i, j))
            for u in adj[i][j]:
                if u not in a_visited:
                    a_stack.append(u)
            else:
                atlantic.add((i, j))

        return [[i, j] for i, j in pacific.intersection(atlantic)]
