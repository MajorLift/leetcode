# Minimum Cost of a Path With Special Roads
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/
# Accepted 2023-05-05 04:12 UTC · Python · 1034 ms · 24.1 MB

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        (xs, ys), (xt, yt) = start, target
        adj = defaultdict(lambda: defaultdict(lambda: +inf))
        nodes = set(map(tuple, (start, target)))
        for x1, y1, x2, y2, w in specialRoads:
            adj[(x1, y1)][(x2, y2)] = min(adj[(x1, y1)][(x2, y2)], w)
            nodes.add((x1, y1))
            nodes.add((x2, y2))
        
        dist = defaultdict(lambda: +inf)
        dist[(xs, ys)] = 0
        pq = [(0, (xs, ys))]
        while pq:
            dist_u, u = heappop(pq)
            if u == target:
                break
            if dist_u > dist[u]:
                continue
            for v in nodes:
                w = min(adj[u][v], self.getCost(u, v))
                if dist_u + w < dist[v]:
                    dist[v] = dist_u + w
                    heappush(pq, (dist[v], v))
        return dist[(xt, yt)]
        
    def getCost(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
