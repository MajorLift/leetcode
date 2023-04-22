# Parallel Courses
# https://leetcode.com/problems/parallel-courses/
# Accepted 2023-04-22 22:13 UTC · Python · 276 ms · 18.6 MB

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj, indegree = [[] for _ in range(n + 1)], [-1] + [0] * n
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1
        starts = [i for i,e in enumerate(indegree) if e == 0]
        if not starts:  # no zero indegree -> entire graph is cycle
            return -1
        
        visited = dict()
        def dfs(node):
            if node in visited:
                return visited[node]
            # base case: leaf node
            if not adj[node]:
                return 1
            # backtracking for cycle detection:
            # -1 is returned iff. upstream node is also found downstream
            visited[node] = -1  # 1) mark
            output = list(map(dfs, [child for child in adj[node]])) # 2) explore
            if any(e == -1 for e in output):    # cycle found
                return -1
            visited[node] = max(output) + 1     # 3) revert
            return visited[node]

        output = list(map(dfs, starts))
        if any(e == -1 for e in output):
            return -1
        return max(output)
