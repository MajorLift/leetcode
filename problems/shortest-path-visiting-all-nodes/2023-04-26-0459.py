# Shortest Path Visiting All Nodes
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# Accepted 2023-04-26 04:59 UTC · Python · 684 ms · 41 MB

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        cache = dict()
        ending_mask = (1 << n) - 1

        def dfs(node, mask):
            if (state := (node, mask)) in cache:  
                return cache[state]    
            if (mask | (1 << node)) == ending_mask:
                return 0
            cache[state] = +inf
            for v in graph[node]:
                if not mask & (1 << v):
                    cache[state] = min(
                        cache[state],
                        1 + dfs(v, mask | 1 << node),   # visited node
                        1 + dfs(v, mask),   # not visited node
                    )
            return cache[state]

        return min(dfs(node, 0) for node in range(n))
