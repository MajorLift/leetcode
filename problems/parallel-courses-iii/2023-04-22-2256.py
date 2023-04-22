# Parallel Courses III
# https://leetcode.com/problems/parallel-courses-iii/
# Accepted 2023-04-22 22:56 UTC · Python · 1593 ms · 43.3 MB

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        time = [0] + time
        adj = [[] for _ in range(n + 1)]
        indegree = [-1] + [0] * n
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1

        dist = [0] * (n + 1)    # single src: null head
        queue = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                # edge weight from 'null head' to zero indegree nodes
                dist[i] = time[i]
                queue.append(i)
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                dist[v] = max(dist[v], dist[u] + time[v])
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return max(dist)
