# House Robber III
# https://leetcode.com/problems/house-robber-iii/
# Accepted 2023-01-31 22:33 UTC · Python · 60 ms · 16.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(node: Optional[TreeNode]):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val
            skips = []
            if node.left:
                skips += [node.left.left, node.left.right]
            if node.right:
                skips += [node.right.left, node.right.right]
            return max(node.val + sum([dp(descendant) for descendant in skips]), sum([dp(node.left), dp(node.right)]))
        return dp(root)
