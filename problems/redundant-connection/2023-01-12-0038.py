# Redundant Connection
# https://leetcode.com/problems/redundant-connection/
# Accepted 2023-01-12 00:38 UTC · Python · 1048 ms · 40.8 MB

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[0 for _ in range(n)] for _ in range(n)]
        for u, v in edges:
            adj[u - 1][v - 1] = 1
            adj[v - 1][u - 1] = 1
        
        def dfs(x, y):
            visited.add(x)
            if x == y:
                return True
            for v, w in enumerate(adj[x]):
                if w == 1 and v not in visited and dfs(v, y):
                    return True
            return False  

        for u, v in edges[::-1]:
            adj[u - 1][v - 1] = 0
            adj[v - 1][u - 1] = 0
            visited = set()
            if dfs(u - 1, v - 1):
                return [u, v]
            adj[u - 1][v - 1] = 1
            adj[v - 1][u - 1] = 1
