# Parallel Courses II
# https://leetcode.com/problems/parallel-courses-ii/
# Accepted 2023-05-02 03:08 UTC · Python · 1164 ms · 23.5 MB

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        adj, indegree = [[] for _ in range(n + 1)], [-inf] + [0] * n
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1

        @cache
        def dp(state=(1 << (n + 1)) - 1, indegree=tuple(indegree)):
            if state == 1: return 0
            starts = [node for node in range(1, n + 1)
                if state & 1 << node and indegree[node] == 0]
            global_min = +inf
            for nodes in combinations(starts, min(k, len(starts))):
                new_state, new_indegree = state, list(indegree)
                for node in nodes:
                    new_state ^= 1 << node
                    for child in adj[node]:
                        new_indegree[child] -= 1
                global_min = min(global_min, 
                    1 + dp(new_state, tuple(new_indegree)))
            return global_min

        return dp()
