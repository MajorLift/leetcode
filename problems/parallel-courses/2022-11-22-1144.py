# Parallel Courses
# https://leetcode.com/problems/parallel-courses/
# Accepted 2022-11-22 11:44 UTC · Python · 277 ms · 17.4 MB

from collections import deque

class Solution:
    # Kahn's algorithm BFS
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in relations:
            adj[u - 1].append(v - 1)
            indegree[v - 1] += 1
        ans = 0
        completed = set()
        queue = deque([node for node in range(n) if indegree[node] == 0])
        while queue:
            ans += 1
            for u in list(queue):
                queue.popleft()
                completed.add(u)
                for v in adj[u]:
                    if v not in completed:
                        indegree[v] -= 1
                        if indegree[v] == 0:
                            queue.append(v)
        return ans if ans >= 0 and len(completed) == n else -1
