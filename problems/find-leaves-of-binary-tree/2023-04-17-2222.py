# Find Leaves of Binary Tree
# https://leetcode.com/problems/find-leaves-of-binary-tree/
# Accepted 2023-04-17 22:22 UTC · Python · 28 ms · 13.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.head = TreeNode(None, root)
        output = []
        while not self.isRootNull():
            output.append(self.dfs(root))
        return output

    def nullRoot(self):
        self.head.left = None

    def isRootNull(self):
        return self.head.left is None

    def dfs(self, root):
        if not root:
            return []
        if self.isLeaf(root):
            self.nullRoot()
            return [root.val]
        leftChild, rightChild = root.left, root.right
        if self.isLeaf(leftChild):
            root.left = None
        if self.isLeaf(rightChild):
            root.right = None
        return ([leftChild.val] 
                if self.isLeaf(leftChild)
                else self.dfs(leftChild)) \
            + ([rightChild.val] 
                if self.isLeaf(rightChild)
                else self.dfs(rightChild))
    
    def isLeaf(self, node):
        return node and not node.left and not node.right
