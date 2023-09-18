# Shortest Path Visiting All Nodes
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# Accepted 2023-09-18 02:21 UTC · Python · 236 ms (37.5%) · 21.7 MB (34.69%)

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        pq = [(0, i, 1 << i) for i in range(n)]
        visited = set(pq)
        while pq:
            steps, u, mask = heappop(pq)
            if mask == (1 << n) - 1:
                return steps
            for v in graph[u]:
                if (v, mask | (1 << v)) not in visited:
                    visited.add((v, mask | (1 << v)))
                    pq.append((steps + 1, v, mask | (1 << v)))
