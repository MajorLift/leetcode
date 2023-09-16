# Minimum Edge Reversals So Every Node Is Reachable
# https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/
# Accepted 2023-09-16 16:59 UTC · Python · 2985 ms (25%) · 367.4 MB (25%)

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_forward, adj_backward = [[] for _ in range(n)], [[] for _ in range(n)]
        for u, v in edges:
            adj_forward[u].append((v, 0))
            adj_backward[v].append((u, 1))
        
        @cache
        def dfs(node, parent):
            return sum(w + dfs(v, node) 
                       for v, w in adj_forward[node] + adj_backward[node] 
                       if v != parent)
        
        return [dfs(i, -1) for i in range(n)]
