# Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/
# Accepted 2023-04-30 18:28 UTC · Python · 313 ms · 25.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.lo, self.hi = low, high
        return self.dfs(root)
        
    def dfs(self, curr):
        if not curr:
            return 0
        return (curr.val 
            if self.lo <= curr.val <= self.hi 
            else 0) \
            + sum(list(map(
                self.dfs, 
                (curr.left, curr.right))))
