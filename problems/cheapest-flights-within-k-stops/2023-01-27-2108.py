# Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Accepted 2023-01-27 21:08 UTC · Python · 128 ms · 15.4 MB

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[0] * n for _ in range(n)]
        for u, v, w in flights:
            adj[u][v] = w

        dist = [(+math.inf, +math.inf)] * n
        dist[src] = (0, 0)
        pq = [(0, 0, src)]
        while pq:
            cost, stops, u = heappop(pq)
            if u == dst:
                break
            for v, w in enumerate(adj[u]):
                if w > 0:
                    min_cost_v, min_stops_v = dist[v]
                    if cost + w < min_cost_v:
                        dist[v] = (cost + w, stops)
                    if (cost + w < min_cost_v or stops < min_stops_v) and stops < k:
                        heappush(pq, (cost + w, stops + 1, v))
                
        return dist[dst][0] if dist[dst][0] < +math.inf else -1
