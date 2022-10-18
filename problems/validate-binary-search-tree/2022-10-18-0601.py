# Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Accepted 2022-10-18 06:01 UTC · Python · 99 ms · 16.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, hi, lo):
            return lo < node.val < hi and (not node.left or validate(node.left, node.val, lo)) and (not node.right or validate(node.right, hi, node.val))
        return validate(root, math.inf, -math.inf)
