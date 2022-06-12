# N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# Accepted 2022-06-12 03:12 UTC · Python · 90 ms · 15.9 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []
        if not root:
            return
        stack = [root]
        while stack:
            curr = stack.pop()
            output.append(curr.val)
            for node in curr.children:
                if node:
                    stack.append(node)
        return output[::-1]
