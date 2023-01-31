# Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Accepted 2023-01-31 01:30 UTC · Python · 110 ms · 15.3 MB

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
                cost_v, stops_v = cost_u + w, stops_u + 1
                
                if (cost_v < min_cost_v 
                    or (cost_v == min_cost_v and stops_v < min_stops_v)):
                    dist[v] = (cost_v, stops_v)

                if (stops_v <= k
                    and (cost_v < min_cost_v or stops_v < min_stops_v)):
                    heappush(pq, (cost_v, stops_v, v))
        
        min_cost_to_dst = dist[dst][0]
        return min_cost_to_dst if min_cost_to_dst < +math.inf else -1
