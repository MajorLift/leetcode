# Parallel Courses
# https://leetcode.com/problems/parallel-courses/
# Accepted 2023-05-01 04:22 UTC · Python · 276 ms · 20.4 MB

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj, indegree = [[] for _ in range(n + 1)], [+inf] + [0] * n
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1
        
        ans = 0
        visited = set()
        queue = [i for i,e in enumerate(indegree) if e == 0]
        while queue:
            ans += 1
            nxt_queue = []
            for u in queue:
                visited.add(u)
                for v in adj[u]:
                    if v in visited:
                        continue
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        nxt_queue.append(v)
            queue = nxt_queue
        return ans if len(visited) == n else -1
