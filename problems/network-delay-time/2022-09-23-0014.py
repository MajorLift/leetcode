# Network Delay Time
# https://leetcode.com/problems/network-delay-time/
# Accepted 2022-09-23 00:14 UTC · Python · 1078 ms · 16.5 MB

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in times:
            adj[u - 1].append((v - 1, w))
        k -= 1
        
        dist = [math.inf if i != k else 0 for i in range(n)]
        pq = [(0, k)]
        while pq:
            dist_u, u = heapq.heappop(pq)
            for v, dist_v in adj[u]:
                if dist_u + dist_v < dist[v]:
                    dist[v] = dist_u + dist_v
                    heapq.heappush(pq, (dist[v], v))
        return max(dist) if all(time < math.inf for time in dist) else -1
