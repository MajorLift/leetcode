# Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Accepted 2023-01-31 01:35 UTC · Python · 99 ms · 15.2 MB

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[0] * n for _ in range(n)]
        for u, v, w in flights:
            adj[u][v] = w

        dist = [(+math.inf, +math.inf)] * n
        dist[src] = (0, 0)
        pq = [(*dist[src], src)]
        while pq:
            cost_u, stops_u, u = heappop(pq)
            if u == dst:
                break

            for v, w in enumerate(adj[u]):
                if w == 0:
                    continue

                min_cost_v, min_stops_v = dist[v]
                cost_uv, stops_uv = cost_u + w, stops_u + 1
                
                if (cost_uv < min_cost_v 
                    or (cost_uv == min_cost_v and stops_uv < min_stops_v)):
                    dist[v] = (cost_uv, stops_uv)

                if ((cost_uv < min_cost_v or stops_uv < min_stops_v) 
                    and stops_uv <= k):
                    heappush(pq, (cost_uv, stops_uv, v))
        
        min_cost_to_dst = dist[dst][0]
        return min_cost_to_dst if min_cost_to_dst < +math.inf else -1
