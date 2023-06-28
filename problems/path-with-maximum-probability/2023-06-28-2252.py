# Path with Maximum Probability
# https://leetcode.com/problems/path-with-maximum-probability/
# Accepted 2023-06-28 22:52 UTC · Python · 656 ms · 28 MB

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[] for _ in range(n)]
        for (u, v), w in zip(edges, succProb):
            adj[u].append((v, w))
            adj[v].append((u, w))
        dist = [0.0] * n
        dist[start] = 1.0
        pq = [(-1.0, start)]
        while pq:
            dist_u, u = heappop(pq)
            dist_u *= -1
            if u == end:
                return dist_u
            for v, dist_v in adj[u]:
                if dist_v == 0.0: continue
                if dist_u * dist_v > dist[v]:
                    dist[v] = dist_u * dist_v
                    heappush(pq, (-dist[v], v))
        return 0
