# Largest Color Value in a Directed Graph
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
# Accepted 2023-04-30 02:33 UTC · Python · 3011 ms · 202.2 MB

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n, m = map(len, (colors, edges))
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
        
        ans = -1
        visited, cycle, cnt = set(), set(), [[0] * 26 for _ in range(n)]
        def dfs(node):
            nonlocal ans
            if node in cycle:
                return True
            if node in visited:
                return False
            visited.add(node)
            cycle.add(node)
            for v in adj[node]:
                if dfs(v):
                    return True
                for color in range(26):
                    cnt[node][color] = max(cnt[node][color], cnt[v][color])
            cycle.remove(node)
            cnt[node][ord(colors[node]) - ord("a")] += 1
            ans = max(ans, cnt[node][ord(colors[node]) - ord("a")])
            return False
        
        for i in range(n):
            if i not in visited:
                if dfs(i):
                    return -1
        return ans
