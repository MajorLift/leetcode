# Shortest Path Visiting All Nodes
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# Accepted 2023-09-17 03:09 UTC · Python · 683 ms (16.92%) · 24 MB (26.46%)

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        cache = [dict() for _ in range(n)]

        def dfs(node: int, mask: int) -> int:
            if mask ^ (1 << node) == (1 << n) - 1:
                return 0
            if mask in cache[node]:
                return cache[node][mask]
            cache[node][mask] = +inf
            cache[node][mask] = reduce(
                lambda acc, v: min(
                    acc, 
                    1 + dfs(v, mask ^ (1 << node)), 
                    1 + dfs(v, mask)), 
                [v for v in graph[node] if not mask & (1 << v)],
                +inf)
            return cache[node][mask]

        return min(dfs(i, 0) for i in range(n))
