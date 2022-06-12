# Network Delay Time
# https://leetcode.com/problems/network-delay-time/
# Accepted 2022-06-12 02:52 UTC · Python · 520 ms · 16.2 MB

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # convert vertex labels to zero-index
        times = [(u - 1, v - 1, w) for u, v, w in times]
        k -= 1
        
        # deserialize input into graph
        adj_list = [[] for _ in range(n)]
        for source, target, weight in times:
            adj_list[source].append((weight, target))
        
        dist = [float('inf') if i != k else 0 for i in range(n)]
        visited = [False for _ in range(n)]
        pq = [(0, k)]

        while pq:
            dist_v, v = heapq.heappop(pq)
            visited[v] = True
            for weight_u, u in adj_list[v]:
                if not visited[u] and dist[v] + weight_u < dist[u]:
                    dist[u] = dist[v] + weight_u
                    heapq.heappush(pq, (dist[u], u))
            print(dist)
        
        return max(dist) if all(visited) else -1
