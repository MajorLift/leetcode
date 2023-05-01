# Parallel Courses
# https://leetcode.com/problems/parallel-courses/
# Accepted 2023-05-01 04:32 UTC · Python · 286 ms · 20.6 MB

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj, indegree = [[] for _ in range(n + 1)], [+inf] + [0] * n
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1
        
        memo = dict()
        def dfs(u):
            if u in memo:
                return memo[u]
            memo[u] = -1
            res = list(map(dfs, adj[u]))
            if any(e == -1 for e in res):
                return -1
            memo[u] = 1 + max(res or [0])
            return memo[u]

        return max([dfs(i) 
            for i,e in enumerate(indegree) 
            if e == 0] or [-1])
