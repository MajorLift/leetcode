# Step-By-Step Directions From a Binary Tree Node to Another
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
# Accepted 2023-04-25 02:18 UTC · Python · 711 ms · 138.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.root = root
        startPath, destPath = self.findPath(root, startValue), self.findPath(root, destValue)
        lca = root
        i = 0
        while i < len(startPath) and i < len(destPath) \
            and startPath[i] == destPath[i]:
            if startPath[i] == 'L':
                lca = lca.left
            elif startPath[i] == 'R':
                lca = lca.right
            i += 1
        startPath, destPath = startPath[i:], destPath[i:]
        return 'U' * len(startPath) + destPath

    def findPath(self, curr, target, path=[]):
        if not curr:
            return ""
        if curr.val == target:
            return "".join(path)
        lpath, rpath = "", ""
        if curr.left:
            path.append("L")
            lpath = self.findPath(curr.left, target, path)
            path.pop()
        if curr.right:
            path.append("R")
            rpath = self.findPath(curr.right, target, path)
            path.pop()
        return lpath or rpath
