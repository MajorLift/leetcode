# Maximal Network Rank
# https://leetcode.com/problems/maximal-network-rank/
# Accepted 2023-08-20 19:19 UTC · Python · 439 ms · 17.9 MB

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [[0] * n for _ in range(n)]
        for u, v in roads:
            adj[u][v] = adj[v][u] = 1
        return max(sum(adj[i]) + sum(adj[j]) - adj[i][j] 
            for i, j in product(range(n), range(n)) 
            if i < j)
