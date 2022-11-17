# Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Accepted 2022-11-17 05:54 UTC · Python · 154 ms · 15.3 MB

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[0 for _ in range(n)] for _ in range(n)]
        for u, v, w in flights:
            adj[u][v] = w
        # print(adj)
        
        dist = [+math.inf for _ in range(n)]
        min_stops = [+math.inf for _ in range(n)]
        dist[src], min_stops[src] = 0, 0
        pq = [(0, 0, src)]
        while pq:
            # print(dist)
            price, stops, u = heapq.heappop(pq)
            if stops > k:
                continue
            if u == dst:
                break
            for v, w in enumerate(adj[u]):
                if w == 0:
                    continue
                if dist[v] > price + w:
                    dist[v] = price + w
                    heapq.heappush(pq, (dist[v], stops + 1, v))
                    min_stops[v] = stops
                elif stops < min_stops[v]:
                    heapq.heappush(pq, (price + w, stops + 1, v))
        # print(curr_stops)
        return dist[dst] if dist[dst] < +math.inf else -1
