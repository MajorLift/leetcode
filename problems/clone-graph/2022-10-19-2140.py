# Clone Graph
# https://leetcode.com/problems/clone-graph/
# Accepted 2022-10-19 21:40 UTC · Python · 53 ms · 14.3 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    visited = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        self.visited[node] = clone = Node(node.val, [])
        if node.neighbors:
            clone.neighbors = [self.cloneGraph(v) for v in node.neighbors]
        return clone
