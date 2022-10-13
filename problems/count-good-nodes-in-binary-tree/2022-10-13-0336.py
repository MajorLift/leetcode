# Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Accepted 2022-10-13 03:36 UTC · Python · 558 ms · 32.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def recurse(node, prevMax):
            nonlocal count
            if node.val >= prevMax:
                count += 1
            newMax = max(prevMax, node.val)
            if node.left:
                recurse(node.left, newMax)
            if node.right:
                recurse(node.right, newMax)
        recurse(root, root.val)
        return count
