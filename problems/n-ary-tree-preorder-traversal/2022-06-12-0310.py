# N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# Accepted 2022-06-12 03:10 UTC · Python · 78 ms · 16 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# recursive:
# def preorder(self, root: 'Node') -> List[int]:
    # output = []
    # def recurse(parent = root):
    #     output.append(parent.val)
    #     for node in parent.children:
    #         if node:
    #             recurse(node)
    # recurse()
    # return output

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        if not root:
            return output
        stack = [root]
        while stack:
            curr = stack.pop()
            output.append(curr.val)
            for node in curr.children[::-1]:
                if node:
                    stack.append(node)
        return output
