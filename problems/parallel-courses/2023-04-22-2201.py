# Parallel Courses
# https://leetcode.com/problems/parallel-courses/
# Accepted 2023-04-22 22:01 UTC · Python · 272 ms · 18.6 MB

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj, indegree = [[] for _ in range(n + 1)], [+inf] + [0] * n
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1
        
        visited = dict()
        def dfs(node):
            if node in visited:
                return visited[node]
            if not adj[node]:
                return 1
            visited[node] = -1
            output = list(map(dfs, [child for child in adj[node]]))
            if any(e == -1 for e in output):
                return -1
            visited[node] = max(output) + 1
            return visited[node]

        output = list(map(dfs, [i for i,e in enumerate(indegree) if e == 0]))
        if not output or any(e == -1 for e in output):
            return -1
        return max(output)
