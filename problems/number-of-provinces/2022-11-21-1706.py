# Number of Provinces
# https://leetcode.com/problems/number-of-provinces/
# Accepted 2022-11-21 17:06 UTC · Python · 961 ms · 14.3 MB

class UnionFind:
    def __init__(self):
        pass

    def union(self, node: int):
        pass

    def find(self):
        pass

from collections import deque
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        queue = deque()
        ans = 0
        for node in range(n):
            if visited[node] == 0:
                ans += 1
                queue.append(node)
                while queue:
                    u = queue.popleft()
                    visited[u] = 1
                    for v in range(n):
                        if isConnected[u][v] == 1 and visited[v] == 0:
                             queue.append(v)
        return ans
