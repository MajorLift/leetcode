# Detonate the Maximum Bombs
# https://leetcode.com/problems/detonate-the-maximum-bombs/
# Accepted 2023-05-02 02:38 UTC · Python · 879 ms · 18.2 MB

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = [[] for _ in range(n)]
        for i, j in product(range(n), range(n)):
            if i != j and self.inRange(bombs[i], bombs[j]):
                adj[i].append(j)

        def detonate(node):
            visited = set()    
            def dfs(u):
                visited.add(u)
                for v in adj[u]:
                    if v not in visited:
                        dfs(v)
            dfs(node)
            return len(visited)

        return max([detonate(start) 
            for start in range(n)])
        
    def inRange(self, s, t):
        (x1, y1, r1), (x2, y2, r2) = s, t
        return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2
