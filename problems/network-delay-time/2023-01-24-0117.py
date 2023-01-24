# Network Delay Time
# https://leetcode.com/problems/network-delay-time/
# Accepted 2023-01-24 01:17 UTC · Python · 628 ms · 16.5 MB

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u][v] = w
        
        dist = [-math.inf] + [0 if i == k else +math.inf for i in range(1, n + 1)]
        pq = [(dist[k], k)]
        while pq:
            dist_u, u = heappop(pq)
            for v, w in enumerate(adj[u]):
                if w < 0:
                    continue
                if dist_u + w < dist[v]:
                    dist[v] = dist_u + w
                    heappush(pq, (dist[v], v))

        return max(dist) if all(x < +math.inf for x in dist) else -1
