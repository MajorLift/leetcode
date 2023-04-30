# Largest Color Value in a Directed Graph
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
# Accepted 2023-04-30 02:44 UTC · Python · 2768 ms · 78.9 MB

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj, indegree = [[] for _ in range(n)], [0] * n
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        global_max = -1
        queue = deque([i for i,e in enumerate(indegree) if e == 0])
        seen, cnt = 0, [[0] * 26 for _ in range(n)]
        while queue:
            u = queue.popleft()
            seen += 1
            cnt[u][ord(colors[u]) - ord("a")] += 1
            global_max = max(global_max, cnt[u][ord(colors[u]) - ord("a")])
            for v in adj[u]:
                for color in range(26):
                    cnt[v][color] = max(cnt[v][color], cnt[u][color])
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return global_max if seen == n else -1
