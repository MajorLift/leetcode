# Parallel Courses III
# https://leetcode.com/problems/parallel-courses-iii/
# Accepted 2023-05-01 23:44 UTC · Python · 1599 ms · 45.7 MB

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        time = [0] + time
        adj, indegree = [[] for _ in range(n + 1)], [-1] + [0] * n
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1
        
        dist = time[:]
        queue = deque([i for i,e in enumerate(indegree) if e == 0])
        while queue:
            curr = queue.popleft()
            for nxt in adj[curr]:
                dist[nxt] = max(dist[nxt], dist[curr] + time[nxt])
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return max(dist)
