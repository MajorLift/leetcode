# Detonate the Maximum Bombs
# https://leetcode.com/problems/detonate-the-maximum-bombs/
# Accepted 2023-04-22 01:50 UTC · Python · 819 ms · 14.2 MB

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = [[] for _ in range(n)]
        for i, j in product(range(n), range(n)):
            if i != j and self.inRange(bombs[i], bombs[j]):
                adj[i].append(j)

        ans = 0
        for start in range(n):
            queue, visited = deque([start]), set([start])
            while queue:
                curr = queue.popleft()
                for v in adj[curr]:
                    if v not in visited:
                        queue.append(v)
                        visited.add(v)
            ans = max(ans, len(visited))
        return ans
        
    def inRange(self, s, t):
        (x1, y1, r1), (x2, y2, _) = s, t
        return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2
