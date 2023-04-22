# Parallel Courses III
# https://leetcode.com/problems/parallel-courses-iii/
# Accepted 2023-04-22 23:03 UTC · Python · 1775 ms · 136.9 MB

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        time = [0] + time
        adj = [[] for _ in range(n + 1)]
        indegree = [-1] + [0] * n
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1

        @cache
        def dp(node):
            return time[node] + max([dp(child) for child in adj[node]] or [0])

        return max([dp(node) for node in range(1, n + 1) if indegree[node] == 0])
