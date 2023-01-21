# Network Delay Time
# https://leetcode.com/problems/network-delay-time/
# Accepted 2023-01-21 03:50 UTC · Python · 486 ms · 16.6 MB

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u][v] = w
        
        dist = [-math.inf] + [+math.inf for _ in range(n)]
        dist[k] = 0
        
        pq = [(dist[k], k)]
        while pq:
            dist_u, u = heappop(pq)
            for v, w in enumerate(adj[u]):
                if w < 0:
                    continue
                if dist_u + w < dist[v]:
                    dist[v] = dist_u + w
                    heappush(pq, (dist[v], v))

        if all(x < +math.inf for x in dist):
            return max(dist)
        return -1
