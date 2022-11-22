# Parallel Courses
# https://leetcode.com/problems/parallel-courses/
# Accepted 2022-11-22 12:01 UTC · Python · 673 ms · 18.4 MB

class Solution:
    # DFS: longest path + detect cycles
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in relations:
            adj[u - 1].append(v - 1)
            indegree[v - 1] += 1
        
        visited = {}
        def dfs(node):
            if node in visited:
                return visited[node]
            else:
                visited[node] = -1

            max_length = 1  # if no next courses -> 1 semester
            for child in adj[node]:
                length = dfs(child)
                if length == -1:
                    return -1
                else:
                    max_length = max(max_length, length + 1)
            visited[node] = max_length
            return max_length
        
        max_length = -1 # if no zero-indegree courses -> invalid
        for node in [u for u in range(n) if indegree[u] == 0]:
            length = dfs(node)
            if length == -1:
                return -1
            else:
                max_length = max(max_length, length)
        return max_length
