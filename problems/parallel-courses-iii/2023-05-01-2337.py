# Parallel Courses III
# https://leetcode.com/problems/parallel-courses-iii/
# Accepted 2023-05-01 23:37 UTC · Python · 1807 ms · 140.7 MB

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        time = [0] + time
        adj, indegree = [[] for _ in range(n + 1)], [-1] + [0] * n
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1
        
        @cache
        def dfs(node):
            return time[node] + max([dfs(nxt) for nxt in adj[node]] or [0])
        starts = [i for i,e in enumerate(indegree) if e == 0]
        return max(map(dfs, starts))
