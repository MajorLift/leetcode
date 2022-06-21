# Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Accepted 2022-06-21 00:06 UTC · Python · 67 ms · 18.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: Root -> Left-sub-pre -> Right-sub-pre
        # inorder: Left-sub-in -> Root -> Right-sub-in
        self.preorder = preorder
        self.rootmap = {val: idx for idx, val in enumerate(inorder)}
        self.preorder_idx = 0
        return self.arrToNode(0, len(preorder))
            
    def arrToNode(self, left, right):
        if left >= right:
            return
        rootVal = self.preorder[self.preorder_idx]
        self.preorder_idx += 1
        return TreeNode(rootVal, \
            self.arrToNode(left, self.rootmap[rootVal]), \
            self.arrToNode(self.rootmap[rootVal] + 1, right))
